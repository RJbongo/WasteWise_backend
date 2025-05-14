from django.contrib import admin
from .models import BinStatus


@admin.register(BinStatus)
class BinStatusAdmin(admin.ModelAdmin):
    list_display = ['bio_status', 'recyclable_status', 'updated_at']
