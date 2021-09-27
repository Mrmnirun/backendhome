from django.contrib import admin

from .models import SpecialOffer

class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'menu_item', 'number_of_items', 'discount', 'availability')
    list_display_links = ('id', 'title')
    list_filter = ('menu_item',)
    search_fields = ('title', 'description')
    list_per_page = 25

admin.site.register(SpecialOffer, SpecialOfferAdmin)