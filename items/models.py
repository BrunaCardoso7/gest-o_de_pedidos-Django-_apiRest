from django.db import models

# Create your models here.
class Item (models.Model):
    name= models.CharField(max_length=100, null=True, blank=True) 
    price= models.FloatField(null=True, blank=True, default=0.0) 
    created_at = models.DateTimeField(auto_now_add=True)