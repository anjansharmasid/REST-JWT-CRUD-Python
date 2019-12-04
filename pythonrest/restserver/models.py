from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    age = models.IntegerField(default=16)
