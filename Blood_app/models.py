from django.db import models

# Create your models here.


class Person(models.Model):
    
    name = models.CharField(null=False, max_length=100)
    age = models.IntegerField(null=False) 
    mobile_number = models.CharField(null=True,max_length=100)
    blood_group = models.CharField(null=True,max_length=10)
    division  = models.CharField(null=False,max_length=100)
    district = models.CharField(null=False,max_length=100)
    subdistrict = models.CharField(null=False,max_length=100)
    person_image = models.ImageField(null= True,upload_to='images/')
    lastdonate = models.DateField(null=False)
