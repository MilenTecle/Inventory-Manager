from django import forms
from django.forms import inlineformset_factory
from .models import Inventory, Items, Category



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['name']


class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ['name', 'category']
        labels = {
            'name': 'List name',
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

        if self.instance.pk is None:
            self.fields['name'].required = True



ItemFormset = inlineformset_factory(
    Inventory,
    Items,
    form=ItemsForm,
    fields=['name'],
    extra=1,
    can_delete=False
)