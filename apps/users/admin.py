from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name', 'middle_name', 'age',
        'gender', 'phone_number',
    )