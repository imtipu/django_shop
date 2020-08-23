from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.get_api_root_view().cls.__name__ = "Shop API"
router.get_api_root_view().cls.__doc__ = "Django Shop API"
urlpatterns = [
    path('', include(router.urls)),
    path('', include('shop.api.v1.urls')),
    path('', include('users.api.v1.urls')),
]
