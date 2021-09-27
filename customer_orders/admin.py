from django.contrib import admin
from .models import CustomerOrder


class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ('id','table_no', 'customer', 'restaurant', 'status', 'total_price', 'date_created')
    list_display_links = ('id',)
    list_filter = ('status', 'restaurant')
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
        return super(CustomerOrderAdmin, self).change_view(request, object_id, extra_context=extra_context)


admin.site.register(CustomerOrder, CustomerOrderAdmin)
