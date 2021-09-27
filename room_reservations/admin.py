from django.contrib import admin

from .models import RoomReservation


class RoomReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'customer', 'payment_status', 'start_date', 'end_date', 'checked_in', 'checked_out')
    list_display_links = ('id', 'room')
    list_filter = ('room', ) # 'payment_status', 'checked_in', 'checked_out'
    search_fields = ('customer_review',)
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
        return super(RoomReservationAdmin, self).change_view(request, object_id, extra_context=extra_context)


admin.site.register(RoomReservation, RoomReservationAdmin)