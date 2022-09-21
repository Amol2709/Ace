from tkinter.tix import Balloon
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class FarmerInfo(models.Model):
    first_name =    models.CharField(max_length=50)
    last_name =     models.CharField(max_length=50, null=True)
    state_name =    models.CharField(max_length=50, null=True)
    district_name = models.CharField(max_length=50, null=True)
    village_name =  models.CharField(max_length=50, null=True)
    phone =         PhoneNumberField()

    text_column_1 = models.TextField(null=True)
    text_column_2 = models.TextField(null=True)
    text_column_3 = models.TextField(null=True)
    text_column_4 = models.TextField(null=True)
    
