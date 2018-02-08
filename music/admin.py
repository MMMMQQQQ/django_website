from django.contrib import admin
from .models import Album

# import the song in the page admin
from .models import Song
# we should tell python that Album should have a admin interface
admin.site.register(Album)
# Register your models here.
admin.site.register(Song)
