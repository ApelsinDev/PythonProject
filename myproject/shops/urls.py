from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CityViewSet, StreetViewSet, ShopViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'streets', StreetViewSet)
router.register(r'shops', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
