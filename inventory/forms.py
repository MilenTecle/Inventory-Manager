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
        labels = {
            'name': 'Item'
        }

    def  __init__(self, *args, **kwargs):
        super(ItemsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'item-name'})
        if self.instance.pk:
            self.fields['name'].widget.attrs['readonly'] = 'readonly'

ItemFormset = inlineformset_factory(
    Inventory,
    Items,
    form=ItemsForm,
    fields=['name'],
    extra=1,
    can_delete=False
)