from django.contrib import admin
from .models import Services, Booking
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
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
    list_display = ('username', 'service_name', 'dog_name',
                    'date_of_booking', 'appointment_time', 'confirmed')
    list_filter = ('username', 'dog_name', 'date_of_booking')
    search_fields = ['username', 'dog_name']
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)
