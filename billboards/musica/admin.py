from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Lista, Cancion

# Register your models here.

admin.site.register(Lista)
admin.site.register(Cancion)
