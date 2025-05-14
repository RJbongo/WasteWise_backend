from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import BinStatus
from .serializers import BinStatusSerializer


class BinStatusViewSet(viewsets.ModelViewSet):
    queryset = BinStatus.objects.all()
    serializer_class = BinStatusSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()] 
        return [IsAuthenticated()]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def latest_bin_status(request):
    latest_status = BinStatus.objects.last()
    if latest_status:
        serializer = BinStatusSerializer(latest_status)
        return Response(serializer.data)
    return Response({"detail": "No bin status available."}, status=404)
