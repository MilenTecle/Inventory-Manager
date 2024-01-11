from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Inventory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=255)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name




