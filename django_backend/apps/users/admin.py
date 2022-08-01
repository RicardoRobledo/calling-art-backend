from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    
    list_display = ('id', 'username', 'is_active')
    
    fieldsets = (
    (
        None, {'fields': ('username', 'password', 'is_active')}),
    )


admin.site.register(User, UserAdmin)
