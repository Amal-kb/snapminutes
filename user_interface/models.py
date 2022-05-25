from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass



class user1(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class org(models.Model):
    orgid = models.AutoField(primary_key=True)
    orgname = models.CharField(max_length=20)



class admin1(models.Model):
    adminid = models.AutoField(primary_key=True)
    adminname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    orgid= models.ForeignKey(org, on_delete=models.CASCADE)
    orgname=models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class meeting(models.Model):
    meetingid = models.AutoField(primary_key=True)
    orgid= models.ForeignKey(org, on_delete=models.CASCADE)
    secretary=models.CharField(max_length=50)
    meetingleader=models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    place=models.CharField(max_length=50)
    agenda= models.CharField(max_length=500)  
    absentees = models.CharField(max_length=50)
    speech=models.CharField(max_length=1000)

class usereg(models.Model):
    slno=models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    orgid= models.ForeignKey(org, on_delete=models.CASCADE)
    userid= models.ForeignKey(user1, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)

