from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ParcelCreateForm
from .models import Parcel
from .services import ParcelCreationError, ParcelDraft, ParcelManagementFacade


facade = ParcelManagementFacade()


def dashboard(request):
    return render(request, "paczkomaty/dashboard.html", {"stats": facade.dashboard()})


def parcel_list(request):
    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()
    context = {
        "parcels": facade.list_parcels(query=query, status=status),
        "query": query,
        "selected_status": status,
        "statuses": Parcel.Status.choices,
    }
    return render(request, "paczkomaty/parcel_list.html", context)


def locker_list(request):
    return render(request, "paczkomaty/locker_list.html", {"lockers": facade.list_lockers()})


def parcel_create(request):
    form = ParcelCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        draft = ParcelDraft(**form.cleaned_data)
        try:
            parcel = facade.send_parcel(draft)
        except ParcelCreationError as exc:
            form.add_error(None, str(exc))
        else:
            messages.success(request, f"Nadano przesylke {parcel.tracking_number}.")
            return redirect("paczkomaty:parcel_list")

    return render(request, "paczkomaty/parcel_form.html", {"form": form})


def put_in_locker(request, parcel_id):
    get_object_or_404(Parcel, pk=parcel_id)
    if request.method != "POST":
        return redirect("paczkomaty:parcel_list")

    try:
        parcel = facade.put_in_locker(parcel_id)
    except (Parcel.DoesNotExist, ParcelCreationError) as exc:
        messages.error(request, str(exc))
    else:
        messages.success(request, f"Przesylka {parcel.tracking_number} zostala umieszczona w paczkomacie.")
    return redirect("paczkomaty:parcel_list")


def mark_delivered(request, parcel_id):
    get_object_or_404(Parcel, pk=parcel_id)
    if request.method != "POST":
        return redirect("paczkomaty:parcel_list")

    try:
        parcel = facade.mark_delivered(parcel_id)
    except Parcel.DoesNotExist:
        messages.error(request, "Nie znaleziono przesylki.")
    else:
        messages.success(request, f"Przesylka {parcel.tracking_number} zostala oznaczona jako dostarczona.")
    return redirect("paczkomaty:parcel_list")
