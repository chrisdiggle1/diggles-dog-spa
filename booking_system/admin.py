from django.contrib import admin
from .models import Services, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """
    Register and view the Services model in the Admin area
    """
    list_display = ('service_name', 'cost', 'duration')
    summernote_fields = ('description')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Register and view the Booking model in the Admin area
    """
    list_display = ('username', 'service_name', 'dog_name', 'date_of_booking',
                    'appointment_time', 'status')
    list_filter = ('username', 'service_name', 'dog_name', 'date_of_booking',
                   'status')
    search_fields = ['username__username', 'dog_name']
    actions = ['approve_booking', 'reject_booking']

    def approve_booking(self, request, queryset):
        queryset.update(status='approved')
        self.message_user(request, "Selected bookings have been approved.")

    def reject_booking(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, "Selected bookings have been rejected.")

    approve_booking.short_description = "Approve selected bookings"
    reject_booking.short_description = "Reject selected bookings"
