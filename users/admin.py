from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here. admin 패널에서 user를 보고싶다. 이건 decorater
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""
    #fieldset 안에 들어가는 것이 blueset이 됨.
    fieldsets = UserAdmin.fieldsets + (("Custom Profile", {"fields": ("avatar", "gender", "bio", "birthdate", "language", "currency", "superhost",)},),)