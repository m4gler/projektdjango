from django.contrib import admin

from .models import Courier, Locker, Parcel


@admin.register(Locker)
class LockerAdmin(admin.ModelAdmin):
    list_display = ("code", "city", "address", "capacity", "occupied_slots")
    search_fields = ("code", "city", "address")


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone")
    search_fields = ("full_name", "phone")


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ("tracking_number", "sender_name", "recipient_name", "status", "locker", "courier")
    list_filter = ("status", "locker", "courier")
    search_fields = ("tracking_number", "sender_name", "recipient_name")
