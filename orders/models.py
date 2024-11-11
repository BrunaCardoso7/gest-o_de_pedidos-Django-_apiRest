from django.db import models
from users.models import User
from items.models import Item
# Create your models here.

class Order(models.Model):
    user= models.ForeignKey(User, related_name='orders',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='orders')
    total = models.FloatField(default=0.0)
    create_at = models.DateTimeField(auto_now_add=True)
