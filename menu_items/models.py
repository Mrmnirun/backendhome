from django.db import models
from datetime import datetime
from restaurants.models import Restaurant

class MenuItem(models.Model):
    # room status enum
    APPETIZER = 'appetizer'
    MAIN = 'main'
    DESSERT = 'dessert'
    DRINK = 'drink'
    menu_types = (
        (APPETIZER, 'Appetizer'),
        (MAIN, 'Main'),
        (DESSERT, 'Dessert'),
        (DRINK, 'Drink')
    )

    title = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, null=True, blank=True)
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    type = models.CharField(max_length=10, choices=menu_types, default=MAIN)
    photo_main = models.ImageField(upload_to='photos/menu_items/main')
    photo_1 = models.ImageField(upload_to='photos/menu_items/other', blank=True)
    photo_2 = models.ImageField(upload_to='photos/menu_items/other', blank=True)
    photo_3 = models.ImageField(upload_to='photos/menu_items/other', blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.title)