from django.db import models

class Album(models.Model):
    artist=models.CharField(max_length=300)
    album_title=models.CharField(max_length=150)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=10000)
    def __str__(self):
        return self.artist+'-'+self.album_title+'-'+self.genre+'-'+self.album_logo

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favourite=models.BooleanField(default=False)
    def __str__(self):
        return self.file_type +'-'+ self.song_title
# Create your models here.
