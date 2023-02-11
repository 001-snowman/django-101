from django.db import models

# Create your models here.
class student(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,blank=True,null=True)
    country=models.CharField(max_length=10,blank=True,null=True)