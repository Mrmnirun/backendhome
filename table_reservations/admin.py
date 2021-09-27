from django.contrib import admin
from .models import TableReservation


class TableReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'customer', 'meal_time', 'customer_arrival', 'reserved_date', 'num_of_people', 'date_added')
    list_display_links = ('id', 'restaurant')
    list_filter = ('restaurant', 'meal_time')
    # search_fields = ('restaurant', 'meal_time', 'customer')
    list_per_page = 25

    def has_delete_permission(self, request, obj=None):
        # Disable delete button
        return False

    def has_add_permission(cls, request):
        ''' remove add and save and add another button '''
        return False

    def change_view(self, request, object_id, extra_context=None):
        ''' customize add/edit form '''
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(TableReservationAdmin, self).change_view(request, object_id, extra_context=extra_context)


admin.site.register(TableReservation, TableReservationAdmin)
