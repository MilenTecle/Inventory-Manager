from django import forms
from django.forms import inlineformset_factory
from .models import Inventory, Items, Category

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'category']
        labels = {
            'name': 'List name'
        }

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name']


ItemFormset = inlineformset_factory(
    Inventory,
    Items,
    form=ItemsForm,
    fields=['name'],
    extra=1,
    can_delete=False
)