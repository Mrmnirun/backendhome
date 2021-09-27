from django.contrib import admin

from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'restaurant', 'availability', 'type')
    list_display_links = ('id', 'title')
    list_filter = ('restaurant', 'type')
    search_fields = ('title', 'description', 'type')
    list_per_page = 25

admin.site.register(MenuItem, MenuItemAdmin)
