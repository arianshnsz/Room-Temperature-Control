from django.contrib import admin
from temp_control.models import Room, Weather


class SmartHomeAdmin(admin.ModelAdmin):
    list_display = ['cooler_status', 'heater_status', 'is_automatic']


admin.site.register(Room, SmartHomeAdmin)
admin.site.register(Weather)
