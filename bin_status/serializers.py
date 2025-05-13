from rest_framework import serializers
from .models import BinStatus, Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'api_key', 'created_at']
        read_only_fields = ['id', 'api_key', 'created_at']

class BinStatusSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True) 

    class Meta:
        model = BinStatus
        fields = ['id', 'device', 'bin_type', 'is_full', 'updated_at']
        read_only_fields = ['id', 'device', 'updated_at']

    
    def create(self, validated_data):
       
        device = validated_data.get('device')
        if not device:
            raise serializers.ValidationError("Device is required.")
        return super().create(validated_data)
