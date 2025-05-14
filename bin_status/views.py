from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import BinStatus
from .serializers import BinStatusSerializer

class BinStatusViewSet(viewsets.ModelViewSet):
    queryset = BinStatus.objects.all()
    serializer_class = BinStatusSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]  # Allow unauthenticated POST from IoT
        return [IsAuthenticated()]
