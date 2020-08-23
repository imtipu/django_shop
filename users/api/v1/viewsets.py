from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import *


User = get_user_model()


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny, ]
    http_method_names = ['post', ]
