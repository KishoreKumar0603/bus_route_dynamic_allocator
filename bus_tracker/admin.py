from django.contrib import admin
from .models import BusStop

@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    list_display = ('name', 'passengers_waiting')
