from django.db import models

class signupdatabase(models.Model):
    name=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    password=models.CharField(max_length=128,unique=True,primary_key=True)
    code=models.CharField(max_length=128)
    
class department1(models.Model):
    employeename=models.CharField(max_length=128)
    