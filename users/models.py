from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django_countries.fields import CountryField
# from phone_field import PhoneField


class User(AbstractUser):
    mobile_number = models.CharField(blank=True, max_length=17, help_text='Contact phone number')

    class Meta:
        ordering = ('-date_joined',)


# billing
class CustomerBillingAddress(models.Model):
    user = models.ForeignKey('users.User', related_name='billing_address_user', on_delete=models.CASCADE, null=False)

    house_flat = models.CharField(max_length=32, null=True, blank=True)
    road_no = models.CharField(max_length=32, null=True, blank=True)
    address_line1 = models.CharField(max_length=120, null=False)
    address_line2 = models.CharField(max_length=120, null=True, blank=True)
    mobile_number = models.CharField(blank=True, max_length=17, help_text='Contact phone number')

    city = models.ForeignKey('shop.City', related_name='billing_city', on_delete=models.CASCADE, null=False,
                             help_text='Billing City')
    state = models.ForeignKey('shop.State', related_name='billing_state', on_delete=models.CASCADE, null=False,
                              help_text='Billing State')
    country = CountryField(null=False, help_text='Billing Country')

    postal_code = models.CharField(max_length=20, null=False, help_text='Postal Code')


# shiiping
class CustomerShippingAddress(models.Model):
    user = models.ForeignKey('users.User', related_name='shipping_address_user', on_delete=models.CASCADE, null=False)

    house_flat = models.CharField(max_length=32, null=True, blank=True)
    road_no = models.CharField(max_length=32, null=True, blank=True)
    address_line1 = models.CharField(max_length=120, null=False)
    address_line2 = models.CharField(max_length=120, null=True, blank=True)
    mobile_number = models.CharField(blank=True, max_length=17, help_text='Contact phone number')

    city = models.ForeignKey('shop.City', related_name='shipping_city', on_delete=models.CASCADE, null=False,
                             help_text='Billing City')
    state = models.ForeignKey('shop.State', related_name='shipping_state', on_delete=models.CASCADE, null=False,
                              help_text='Billing State')
    country = CountryField(null=False, help_text='Billing Country')

    postal_code = models.CharField(max_length=20, null=False, help_text='Postal Code')


class ChatRoom(models.Model):
    user_one = models.ForeignKey('users.User', related_name='user_one_room', on_delete=models.CASCADE, null=False)
    user_two = models.ForeignKey('users.User', related_name='user_two_room', on_delete=models.CASCADE, null=False)

    
