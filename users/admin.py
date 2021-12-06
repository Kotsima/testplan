from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, CSV_data

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name']

class CSV_data_admin(admin.ModelAdmin):
    model = CSV_data
    list_display = ['fullname', 'job', 'email_csv', 'domain_name', 'phone_number', 'company_name', 'text', 'integer', 'address', 'data']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CSV_data, CSV_data_admin)