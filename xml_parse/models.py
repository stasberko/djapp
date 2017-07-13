from django.db import models

# Create your models here.


class MediaType(models.Model):
    mtype = models.CharField(max_length=20)


class Stories(models.Model):
    lang = models.CharField(max_length=5)
    keywords = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=30)
    paragraph = models.TextField()


class Headers(models.Model):
    datetime = models.DateTimeField()
    author = models.CharField(max_length=4)
    mediatype = models.ForeignKey(MediaType)
    media = models.TextField()
    country = models.CharField(max_length=4)
    name = models.CharField(max_length=25)
    product = models.CharField(max_length=25)
    term = models.CharField(max_length=25)


class Items(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    status = models.CharField(max_length=15)
    analysis = models.CharField(max_length=4)
    header = models.OneToOneField(Headers)
    story = models.OneToOneField(Stories)