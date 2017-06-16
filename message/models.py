
from django.db import models
from django.conf import settings
# Create your models here.
class Message(models.Model):
    dtime = models.DateTimeField(auto_now_add=True)
    mess = models.CharField(max_length=200)
    auth = models.ForeignKey(settings.AUTH_USER_MODEL)
