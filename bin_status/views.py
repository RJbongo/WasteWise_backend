from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BinStatus, Device
from .serializers import BinStatusSerializer
from rest_framework import serializers
class BinStatusViewSet(viewsets.ModelViewSet):
    queryset = BinStatus.objects.all()
    serializer_class = BinStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        api_key = self.request.headers.get('API-Key')  
        if not api_key:
            raise serializers.ValidationError("API-Key header is missing")
        
        # Fetch the device that matches the API key
        device = Device.objects.filter(api_key=api_key).first()
        if not device:
            raise serializers.ValidationError("Invalid API Key")
        
        # Save the bin status associated with the device
        serializer.save(device=device)

    def get_queryset(self):
        # Use the API key to filter bin statuses by device
        api_key = self.request.headers.get('API-Key')
        if not api_key:
            raise serializers.ValidationError("API-Key header is missing")
        
        device = Device.objects.filter(api_key=api_key).first()
        if not device:
            raise serializers.ValidationError("Invalid API Key")

        return BinStatus.objects.filter(device=device)

    @action(detail=True, methods=['post'])
    def update_bin_status(self, request, pk=None):
        # Optional: A custom action for updating bin status via POST
        bin_status = self.get_object()
        bin_status.is_full = request.data.get('is_full', bin_status.is_full)
        bin_status.save()
        return Response({'status': 'updated'})
