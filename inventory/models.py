from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from cloudinary.models import CloudinaryField
from .utils import generate_qrcode
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True)
    qr_code = models.URLField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.qr_code:
            self.qr_code = generate_qrcode(self.get_url())

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Inventories'
        unique_together = ('user', 'name')

    def get_url(self):
        domain = get_current_site(None).domain
        inventory_id = self.id
        # Ensures that the URL is absolute
        return '{domain}{path}'.format(
            domain=domain,
            path=reverse('saved_list', args=[str(inventory_id)]))

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=255)
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='items')

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
