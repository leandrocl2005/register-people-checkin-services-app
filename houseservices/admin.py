from django.contrib import admin

from houseservices.models import HouseServices


# Register your models here.
@admin.register(HouseServices)
class HouseServicesAdmin(admin.ModelAdmin):
    list_display = ('person', 'breakfast', 'lunch', 'snack', 'dinner',
                    'shower', 'sleep', 'created_at')
