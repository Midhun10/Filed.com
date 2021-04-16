from django.db import models

# Create your models here.
class AudioType(models.Model):
    choice = (
        ('1','Song'),
        ('2','AudioBook'),
        ('3','Podcast')
    )
    audiotype = models.CharField(max_length=25,choices=choice)


class Song(models.Model):
    Song_Name = models.CharField(blank=False,max_length=100,default=None)
    Song_Duration = models.PositiveIntegerField(blank=False,default=None)
    Song_Uploaddate = models.DateField(blank=False,default=None)
    Song_Uploadtime = models.TimeField(blank=False,default=None)

    def __str__(self):
        return self.Song_Name

class AudioBook(models.Model):
    Book_Title = models.CharField(null=False,blank=False,max_length=100)
    Book_Author = models.CharField(null=False,blank=False,max_length=100)
    Book_Narrator = models.CharField(null=False,blank=False,max_length=100)
    Book_Duration = models.PositiveIntegerField(blank=False,default=None)
    Book_Uploaddate = models.DateField(blank=False,default=None)
    Book_Uploadtime = models.TimeField(blank=False,default=None)
    
    def __str__(self):
        return self.Book_Title

class Podcast(models.Model):
    Podcast_Name = models.CharField(null=False,blank=False,max_length=100)
    Podcast_Duration = models.PositiveIntegerField(blank=False,default=None)
    Podcast_Uploaddate = models.DateField(blank=False,default=None)
    Podcast_Uploadtime = models.TimeField(blank=False,default=None)
    Podcast_Host = models.CharField(null=False,blank=False,max_length=100)
    Podcast_Participants_Count = models.PositiveIntegerField(blank=True,default=None)
    Podcast_Participants = models.CharField(blank=True,max_length=100,null=True)

    def __str__(self):
        return self.Podcast_Name