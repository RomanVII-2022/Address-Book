from django.db import models

# Create your models here.
class Address(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
