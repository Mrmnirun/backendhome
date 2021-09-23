from django.db import models

class RoomType(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    number_of_adults = models.IntegerField()
    number_of_beds = models.IntegerField()
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/roomTypes/')
    photo_1 = models.ImageField(upload_to='photos/roomTypes/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/roomTypes/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/roomTypes/', blank=True)

    def __str__(self):
        return self.title