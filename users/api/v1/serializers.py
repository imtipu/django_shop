from allauth.account.adapter import get_adapter
from allauth.account.forms import ResetPasswordForm
from allauth.account.utils import setup_user_email, send_email_confirmation
from allauth.account import app_settings as allauth_settings
from allauth.utils import generate_unique_username, email_address_exists
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

from rest_framework import exceptions, serializers
from django.http import HttpRequest
from rest_auth.serializers import PasswordResetSerializer
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
# from rest_framework_simplejwt.tokens import RefreshToken

from users.models import *

from django.contrib.auth import get_user_model

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    # mobile_number = PhoneNumberField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'mobile_number', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'email': {
                'required': True,
                'allow_blank': False,
            }
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            # name=validated_data.get('name'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            username=generate_unique_username([
                validated_data.get('first_name'),
                validated_data.get('last_name'),
                'user'
            ]),
            is_active=False
        )
        user.set_password(validated_data.get('password'))
        user.save()
        request = self._get_request()
        setup_user_email(request, user, [])
        send_email_confirmation(request, user, signup=True)

        # twilio_send_verification_code(user)
        return user

    def save(self, request=None):

        """rest_auth passes request so we must override to accept it"""
        return super().save()


class UserLoggedSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'date_joined',
        )
