from rest_framework import serializers
from .models import BinStatus

class BinStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinStatus
        fields = ['id', 'bio_status', 'recyclable_status', 'updated_at']
        read_only_fields = ['id', 'updated_at']
