from django.contrib import admin
from .models import *

admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(LikeFilm)
admin.site.register(Rating)