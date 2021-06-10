from django.db import models

class Destination(models.Model):
    name=models.CharField(max_length=100)

class Writer(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=13,null=True)
    address=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=254,null=True)
    dob=models.DateField(null=True)