from django.urls import path

from . import views

app_name = "paczkomaty"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("przesylki/", views.parcel_list, name="parcel_list"),
    path("przesylki/nadaj/", views.parcel_create, name="parcel_create"),
    path("przesylki/<int:parcel_id>/umiesc-w-paczkomacie/", views.put_in_locker, name="put_in_locker"),
    path("przesylki/<int:parcel_id>/dostarcz/", views.mark_delivered, name="mark_delivered"),
    path("paczkomaty/", views.locker_list, name="locker_list"),
]
