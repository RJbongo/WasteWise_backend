from django.contrib import admin
from .models import BinStatus, Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_key']     
    readonly_fields = ['api_key']

@admin.register(BinStatus)
class BinStatusAdmin(admin.ModelAdmin):
    list_display = ['device', 'bin_type', 'is_full', 'updated_at']
