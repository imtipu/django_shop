from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from ..v1 import viewsets

from .views import *

router = DefaultRouter()
router.register(u'account/register', viewsets.SignupViewSet, basename='api_account_register')
urlpatterns = [
    path('', include(router.urls)),
    path('app/customer/login-verify/', CustomerLoginVerify.as_view(), name='shopify_customer_login_verify'),
    path('account/auth-user/', AuthenticatedUserProfile.as_view(), name='auth_user_profile'),
    path('account/login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('account/login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('account/register/', name='api_account_register'),
]
