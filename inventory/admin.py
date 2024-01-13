from django.contrib import admin
from .models import Inventory, Category, Items
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Category)
admin.site.register(Items)
