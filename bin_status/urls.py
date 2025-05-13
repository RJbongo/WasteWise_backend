from rest_framework.routers import DefaultRouter
from .views import BinStatusViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'bin-status', BinStatusViewSet, basename='bin-status')

urlpatterns = [
    path('', include(router.urls)),
]
    