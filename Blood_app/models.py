from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Person(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(null=True, max_length=100)
    age = models.IntegerField(null=True) 
    mobile_number = models.CharField(null=True,max_length=100)
    blood_group = models.CharField(null=True,max_length=10)
    division  = models.CharField(null=True,max_length=100)
    district = models.CharField(null=True,max_length=100)
    subdistrict = models.CharField(null=True,max_length=100)
    person_image = models.ImageField(null= True,upload_to='images/')
    lastdonate = models.DateField(null=True)
