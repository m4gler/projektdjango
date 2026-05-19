from django.core.exceptions import ValidationError
from django.db import models


class Locker(models.Model):
    code = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=160)
    capacity = models.PositiveIntegerField(default=10)

    class Meta:
        ordering = ["city", "code"]

    def __str__(self):
        return f"{self.code} - {self.city}, {self.address}"

    @property
    def occupied_slots(self):
        return self.parcels.filter(status=Parcel.Status.IN_LOCKER).count()

    @property
    def free_slots(self):
        return max(self.capacity - self.occupied_slots, 0)

    def has_free_slot(self):
        return self.free_slots > 0


class Courier(models.Model):
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class Parcel(models.Model):
    class Status(models.TextChoices):
        CREATED = "created", "Utworzona"
        ASSIGNED = "assigned", "Przypisana kurierowi"
        IN_LOCKER = "in_locker", "W paczkomacie"
        DELIVERED = "delivered", "Dostarczona"

    tracking_number = models.CharField(max_length=32, unique=True)
    sender_name = models.CharField(max_length=120)
    recipient_name = models.CharField(max_length=120)
    recipient_phone = models.CharField(max_length=20)
    locker = models.ForeignKey(Locker, related_name="parcels", on_delete=models.PROTECT)
    courier = models.ForeignKey(Courier, related_name="parcels", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CREATED)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.tracking_number

    def clean(self):
        if self.status == self.Status.IN_LOCKER and not self.locker.has_free_slot():
            raise ValidationError("Wybrany paczkomat nie ma wolnych skrytek.")
