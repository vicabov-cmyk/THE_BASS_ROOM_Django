import uuid
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.title

class Guest(models.Model):
    GUEST_TYPES = [
        ("regular", "Постійний"),
        ("one_time", "Разовий"),
    ]

    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    guest_type = models.CharField(
        max_length=20,
        choices=GUEST_TYPES,
        default="one_time"
    )

    def __str__(self):
        return self.full_name

class Ticket(models.Model):
    order_reference = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE,
        related_name="tickets"
    )
    guest = models.ForeignKey(
        Guest, on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=8, decimal_places=2,
        default=350
    )
    is_paid = models.BooleanField(default=False)
    is_checked_in = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest} - {self.event}"
