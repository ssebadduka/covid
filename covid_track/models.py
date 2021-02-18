from django.db import models
from django.utils import  timezone
import  datetime

# Create your models here.
class Patient_info(models.Model):
    sex = [
        ('Male','Male'),
        ('Female','Female')
    ]
    date_registered = models.DateTimeField(timezone.now)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    gender = models.CharField(choices=sex,default='Male')
    Date_of_birth = models.DateTimeField()
    nationality = models.CharField(max_length= 45)
    phone = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    



