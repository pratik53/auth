from pyexpat import model
from django.db import models

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length = 10)
    email = models.EmailField(null = True)
    image = models.ImageField(null = True)