from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id','username', 'email', 'phone_number', 'bio', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone_number', 'bio',)}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
