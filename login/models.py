from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth
from datetime import date
from datetime import datetime


# Create your models here.

class recharge(models.Model): 
    uname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    service_no=models.IntegerField() 
    s_provider = models.CharField(max_length=100)
    amount = models.IntegerField()
    status=models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.s_provider

    #description = models.TextField(blank=True)
# class drecharge(models.Model):
#     uname = models.CharField(max_length=100)
#     fname = models.CharField(max_length=100)
#     cardno = models.IntegerField()
#     s_provider = models.CharField(max_length=100)
#     amount = models.IntegerField()    
class wallet(models.Model):
    c_bal=models.IntegerField()
    ad_money=models.IntegerField()

   
class complaints(models.Model):
    uname=models.CharField(max_length=100)
    spname =models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    complaint = models.CharField(max_length=100)
    details = models.TextField() 
    replay = models.TextField()
    status =models.TextField()
    
    
    

    # def __str__(self):
    #      return self.uname
    

class spweb(models.Model):
    we=models.CharField(max_length=100)
class offer(models.Model):  
    spname=models.CharField(max_length=100)
    sname=models.CharField(max_length=100)
    ofr_dtls=models.CharField(max_length=200)

    def __str__(self):
        return self.sname
  


class serviceprovider(models.Model):
    uname=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    website=models.CharField(max_length=100)
    mob=models.IntegerField()
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class userregistration(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mob=models.IntegerField()
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.fname    


    