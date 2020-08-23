from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile_number', 'is_active', 'is_staff', 'is_superuser', 'date_joined']
