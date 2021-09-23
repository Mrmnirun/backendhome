from django.db import models
from datetime import datetime
from room_types.models import RoomType
from django.contrib.auth.models import User

class Room(models.Model):
    # room status enum
    OCCUPIED = 'occupied'
    VACANT = 'vacant'
    room_statuses = (
        (OCCUPIED, 'Occupied'),
        (VACANT, 'Vacant')
    )

    room_number = models.IntegerField()
    floor_number = models.IntegerField()
    type = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=10, choices=room_statuses, default=VACANT)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    customer_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return str(self.room_number)
