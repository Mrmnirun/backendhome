from django.contrib import admin

from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_number', 'floor_number', 'type', 'status', 'customer_id')
    list_display_links = ('id', 'room_number')
    list_filter = ('floor_number', 'type', 'status')
    search_fields = ('room_number', 'floor_number', 'status')
    list_per_page = 25

admin.site.register(Room, RoomAdmin)
