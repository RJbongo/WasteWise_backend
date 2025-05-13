from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import DeviceAPIKey

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return None  # Let other auth classes try

        try:
            key_obj = DeviceAPIKey.objects.get(api_key=api_key, active=True)
        except DeviceAPIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid or inactive API key')

        return (None, None)  # No user associated, just authenticates the device
