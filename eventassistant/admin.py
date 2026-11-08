from django.contrib import admin
from .models import Event, Guest, Ticket

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "capacity")

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "guest_type")
    list_filter = ("guest_type",)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "guest", "event", "price",
        "is_paid", "is_checked_in"
    )
    list_filter = ("event", "is_paid", "is_checked_in")
    list_editable = ("is_paid", "is_checked_in")
