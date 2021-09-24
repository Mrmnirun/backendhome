from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant
from datetime import datetime
from middleware.enums.order_status_enum import order_statuses


class CustomerOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, null=True)
    table_no = models.IntegerField(default=1)
    status = models.CharField(max_length=50, choices=order_statuses, default=order_statuses[0][0])
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    menu_items = models.CharField(default="{}", max_length=255)
    special_offers = models.CharField(default="{}", max_length=255)
    date_created = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return str(self.id)