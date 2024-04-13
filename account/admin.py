from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import UserCreation
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserCreation
    model = CustomUser
    list_display = ["email", "username", "girlfriend", "is_staff"]
   
    
admin.site.register(CustomUser,  CustomUserAdmin)
