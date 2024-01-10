from django.db import models
from django.contrib.auth.models import get_user_model
from cloudinary.models import CloudinaryField

# Create your models here.
class Inventory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models)

    def __str__(self):
        return self.name