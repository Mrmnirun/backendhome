from django.contrib import admin

from .models import RoomType


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')
    list_filter = ('number_of_adults', 'number_of_beds')
    search_fields = ('title', 'description')
    list_per_page = 25


admin.site.register(RoomType, RoomTypeAdmin)
