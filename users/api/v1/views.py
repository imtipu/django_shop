from django.http import HttpResponse, Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.api.v1.serializers import *


def account_login(request):
    return HttpResponse(0)


class AuthenticatedUserProfile(RetrieveAPIView, UpdateAPIView):
    authentication_classes = [JWTAuthentication,
                              SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserLoggedSerializer

    def get_object(self):
        try:
            return User.objects.get(pk=self.request.user.id)
        except User.DoesNotExist:
            raise Http404

    
