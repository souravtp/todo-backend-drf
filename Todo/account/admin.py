from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token

from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        # Delete associated tokens before deleting users
        for user in queryset:
            # Delete associated tokens
            Token.objects.filter(user=user).delete()

        # Now delete the users
        super().delete_queryset(request, queryset)

    def delete_view(self, request, object_id, extra_context=None):
        # Convert object_id to user_id
        user_id = object_id
        # Delete associated tokens
        Token.objects.filter(user_id=user_id).delete()
        # Now call the original delete_view
        return super().delete_view(request, object_id, extra_context)
