from django.contrib import admin

from .models import BookingDetails, Visitors, RtkPresent


@admin.register(RtkPresent)
class RtkPresent(admin.ModelAdmin):
    list_display = (
        'machine_model',
        'machine_description',
        'machine_daily_rate',
    )


# admin.site.register(BookingDetails)

@admin.register(BookingDetails)
class BookingDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'machine_booked',
        'name_of_person_booking',
        'phone_of_person_booking',
        'email_of_person_booking',
        'project_location',
    )

@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = (
        'ip_addres_of_visitor',
        'session_id',
        'user_agent',
        'visiting_time')
# admin.site.register(Visitors)

# Register your models here.
