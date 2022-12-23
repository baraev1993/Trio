from django.contrib import admin
from .models import Category,Film



class FilmAdmin(admin.ModelAdmin):
    list_display = ['name','category']
    list_filter = ['category' , 'id']
    search_fields =['name','description']


admin.site.register(Category)
admin.site.register(Film,FilmAdmin)


