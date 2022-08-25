from asyncio.windows_events import NULL
from django.db import models
from django.forms import CharField, DateField

# Create your models here.

class Information(models.Model):

    list=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    discription=models.CharField(max_length=260)
    date=models.DateField()
