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

class Criminal(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=254,null=True)
    occupation=models.CharField(max_length=50,null=True)
    dob=models.DateField(null=True)

class Victim(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=254,null=True)
    occupation=models.CharField(max_length=50,null=True)
    dob=models.DateField(null=True)
    
class FIR(models.Model):
    FIR_Title=models.CharField(max_length=100,null=True)
    FIR_Type=models.CharField(max_length=100,null=True)
    Victim_Name=models.CharField(max_length=50,null=True)
    Victim_Age=models.CharField(max_length=2,null=True)
    Victim_Address=models.CharField(max_length=100,null=True)
    FIR_Description= models.TextField(null=True)
    FIR_Date=models.DateField(null=True)
    Incident_Time=models.TimeField()
    Incident_Place=models.CharField(max_length=100,null=True)
