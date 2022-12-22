from django.contrib import admin
from main.models import Category,Film
from .models import User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Film)
