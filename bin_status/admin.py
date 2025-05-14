from django.contrib import admin
from .models import BinStatus
from django.contrib.auth.models import User

@admin.register(BinStatus)
class BinStatusAdmin(admin.ModelAdmin):
    list_display = ['bio_status', 'recyclable_status', 'updated_at']


admin.site.register(User)