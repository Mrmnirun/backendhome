from django.contrib import admin

from .models import RoomReservation

class RoomReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'customer', 'payment_status', 'start_date', 'end_date', 'checked_in', 'checked_out')
    list_display_links = ('id', 'room')
    list_filter = ('room', 'customer', 'payment_status', 'checked_in', 'checked_out')
    search_fields = ('room', 'customer', 'total_price', 'customer_review')
    list_per_page = 25

admin.site.register(RoomReservation, RoomReservationAdmin)