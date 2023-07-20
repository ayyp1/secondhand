from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Bike(models.Model):
    def     __str__(self):
        return self.name 
    seller_name = models.ForeignKey(User , on_delete=models.CASCADE,default=1) #to add sellers name 
    name  = models.CharField(max_length= 100)
    desc = models.CharField(max_length= 200)
    bikenum = models.IntegerField()
   
    image = models.ImageField(blank=True,upload_to='images')
    ordering = ['-created_at']