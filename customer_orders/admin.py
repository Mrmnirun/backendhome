from django.contrib import admin
from .models import CustomerOrder

class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ('id','table_no', 'customer', 'restaurant', 'status', 'total_price', 'date_created')
    list_display_links = ('id',)
    list_filter = ('status',)
    search_fields = ('meal_time', 'status', 'restaurant', 'table_no')
    list_per_page = 25

admin.site.register(CustomerOrder, CustomerOrderAdmin)
