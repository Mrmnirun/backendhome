from django.contrib import admin

from .models import Restaurant


class RestaurantTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'floor_number', 'type', 'status', 'number_of_tables', 'breakfast', 'lunch', 'dinner')
    list_display_links = ('id', 'title')
    list_filter = ('floor_number', 'status', 'type')
    search_fields = ('title', 'status', 'description', 'type', 'number_of_tables', 'floor_number')
    list_per_page = 25


admin.site.register(Restaurant, RestaurantTypeAdmin)
