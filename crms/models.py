from django.db import models

class Destination(models.Model):
    name=models.CharField(max_length=100)

class Writer(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
# Create your models here.
