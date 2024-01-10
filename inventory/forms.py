from django import forms
from .models import Inventory, Items, Category

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'category']

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'inventory']