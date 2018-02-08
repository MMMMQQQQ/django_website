from django.db import models
from django.urls import reverse

# Create your models here.
#Red pk 1
class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})
    def __str__(self):
        return self.album_title+'-'+self.artist

# to create teh simple form, we need to change the song class, the song needs another attribute
# then we update in the model
class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_facorite=models.BooleanField(default=False)


# the song has associated with the album, before we do, we should create a representation for the song
    def __str__(self):
        return self.song_title


# because now we have the model, so we should synchronize the data
# to add changes to the site of the administeur of the song, we should add in the terminal:"python manage.py shell" then "import music.models import Album, Song"
# then we use "song=Song()" to define a variable of song, and then add the attribute of song
# use "song.save()"to save the changes in the database

#another way to add the song data in the database:
# album1.song_set.all() to see all the song in the database
# album1.song_set.create(song_title='I love bacon',file_type='mp3')
