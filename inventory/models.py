from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from cloudinary.models import CloudinaryField
from .utils import generate_qrcode
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Inventory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    qr_code = models.URLField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.qr_code:
            self.qr_code = generate_qrcode(self.name, self.pk, request)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Inventories'

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=255)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='items')

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name




