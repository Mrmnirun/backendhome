from django.db import models
from restaurants.models import Restaurant
from django.contrib.auth.models import User
from datetime import datetime


class TableReservation(models.Model):
    # meal time enum
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    meal_times = (
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner')
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, null=True)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    meal_time = models.CharField(max_length=50, choices=meal_times, default=BREAKFAST)
    num_of_people = models.IntegerField(default=1)
    reserved_date = models.DateField(blank=True)
    customer_arrival = models.BooleanField(default=False)
    date_added = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return str(self.id)
