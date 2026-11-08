from django.urls import path
from .views import (
    dashboard,
    event_create,
    guest_create,
    ticket_create,
    event_edit,
    event_delete,
)

urlpatterns = [
    path("", dashboard, name="eventassistant_dashboard"),
    path("create/", event_create, name="event_create"),
    path("guest/create/", guest_create, name="guest_create"),
    path("event/<int:pk>/edit/", event_edit, name="event_edit"),
    path("ticket/create/", ticket_create, name="ticket_create"),
    path("event/<int:pk>/delete/", event_delete, name="event_delete"),
]