from django.db import models
from rooms.models import Room
from django.contrib.auth.models import User


class RoomReservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, null=True)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    checked_in = models.BooleanField(default=False)
    checked_out = models.BooleanField(default=False)
    customer_review = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)