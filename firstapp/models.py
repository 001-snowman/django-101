from django.db import models

# Create your models here.
class student(models.Model):
    fname=models.CharField(max_length=50, blank=True, null=True)
    lname=models.CharField(max_length=50, blank=True, null=True)
    gender=models.CharField(max_length=1, blank=True, null=True)
    country=models.CharField(max_length=10, blank=True, null=True)