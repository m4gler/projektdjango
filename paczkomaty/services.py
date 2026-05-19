from dataclasses import dataclass
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.db.models import Q

from .models import Courier, Locker, Parcel


class ParcelCreationError(Exception):
    pass


@dataclass(frozen=True)
class ParcelDraft:
    sender_name: str
    recipient_name: str
    recipient_phone: str
    locker: Locker
    courier: Courier | None = None


class ParcelFactory:
    """Factory Method: tworzy spojny obiekt przesylki z numerem sledzenia."""

    prefix = "PCK"

    def create(self, draft: ParcelDraft) -> Parcel:
        return Parcel(
            tracking_number=self._tracking_number(),
            sender_name=draft.sender_name,
            recipient_name=draft.recipient_name,
            recipient_phone=draft.recipient_phone,
            locker=draft.locker,
            courier=draft.courier,
            status=Parcel.Status.ASSIGNED if draft.courier else Parcel.Status.CREATED,
        )

    def _tracking_number(self):
        return f"{self.prefix}-{uuid4().hex[:10].upper()}"


class ParcelManagementFacade:
    """Facade: ukrywa operacje ORM potrzebne widokom aplikacji."""

    def __init__(self, factory=None):
        self.factory = factory or ParcelFactory()

    def dashboard(self):
        return {
            "lockers": Locker.objects.count(),
            "couriers": Courier.objects.count(),
            "parcels": Parcel.objects.count(),
            "in_lockers": Parcel.objects.filter(status=Parcel.Status.IN_LOCKER).count(),
            "delivered": Parcel.objects.filter(status=Parcel.Status.DELIVERED).count(),
            "recent_parcels": Parcel.objects.select_related("locker", "courier")[:5],
        }

    def list_parcels(self, query="", status=""):
        parcels = Parcel.objects.select_related("locker", "courier").all()

        if query:
            parcels = parcels.filter(
                Q(tracking_number__icontains=query)
                | Q(sender_name__icontains=query)
                | Q(recipient_name__icontains=query)
                | Q(recipient_phone__icontains=query)
            )

        if status in Parcel.Status.values:
            parcels = parcels.filter(status=status)

        return parcels

    def list_lockers(self):
        return Locker.objects.prefetch_related("parcels").all()

    @transaction.atomic
    def send_parcel(self, draft: ParcelDraft):
        if not draft.locker.has_free_slot():
            raise ParcelCreationError("Wybrany paczkomat nie ma wolnych skrytek.")

        parcel = self.factory.create(draft)
        try:
            parcel.full_clean()
            parcel.save()
        except (ValidationError, IntegrityError) as exc:
            raise ParcelCreationError("Nie udalo sie nadac przesylki. Sprawdz dane i sproboj ponownie.") from exc

        return parcel

    @transaction.atomic
    def put_in_locker(self, parcel_id):
        parcel = Parcel.objects.select_related("locker").get(pk=parcel_id)
        if not parcel.locker.has_free_slot():
            raise ParcelCreationError("Brak wolnych skrytek w paczkomacie.")
        parcel.status = Parcel.Status.IN_LOCKER
        parcel.full_clean()
        parcel.save(update_fields=["status"])
        return parcel

    @transaction.atomic
    def mark_delivered(self, parcel_id):
        parcel = Parcel.objects.get(pk=parcel_id)
        parcel.status = Parcel.Status.DELIVERED
        parcel.full_clean()
        parcel.save(update_fields=["status"])
        return parcel
