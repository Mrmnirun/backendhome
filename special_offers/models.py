from django.db import models
from datetime import datetime
from menu_items.models import MenuItem

class SpecialOffer(models.Model):
    title = models.CharField(max_length=255)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING, null=True, blank=True)
    number_of_items = models.IntegerField()
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/special_offers/')
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.title)