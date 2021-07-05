from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from customer.models import CustomerModel
# Register your models here.
@admin.register(CustomerModel)
class Customadmin(UserAdmin):
    fieldsets=UserAdmin.fieldsets+(
        ('avataralan',{'fields': ('avatar',)}),
    )

