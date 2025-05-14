from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import BinStatus
from .serializers import BinStatusSerializer

class BinStatusViewSet(viewsets.ModelViewSet):
    queryset = BinStatus.objects.all().order_by('-created_at')  # Order by creation date
    serializer_class = BinStatusSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Anyone can fetch data
        return [IsAuthenticated()]  # Only authenticated users can create, update, delete

    def list(self, request, *args, **kwargs):
        # Override the list method to return only the latest bin status
        latest_status = BinStatus.objects.last()
        if latest_status:
            serializer = self.get_serializer(latest_status)
            return Response(serializer.data)
        return Response({"detail": "No bin status available."}, status=404)
