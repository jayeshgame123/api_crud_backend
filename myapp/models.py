from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    email = models.EmailField(max_length=254)
    mobile = models.BigIntegerField()