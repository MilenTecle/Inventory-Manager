from django import forms
from django.forms import inlineformset_factory
from django.db.models import Q
from .models import Inventory, Items, Category


"""
A form for creating and editing Categories. The form is linked to the Category model
and allows users to specify the name of a category.
"""
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['name']


"""
A form for creating and editing Inventories. The form is associated with the Inventory Model.
It allow users to specify the name of the inventory list and its category using a dropdown menu, including
a placeholder. A "General" category is also provided to the user so the user quickly can create a list,
and then change and/or add a category as desired.
"""
class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ['name', 'category']
        labels = {
            'name': 'List name',
            'category': 'Category'
        }


    def  __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(Q(user=user) | Q(user=None))
            self.fields['category'].empty_label = "--Select category--"



"""
A form for creating and editing Items.
The form is linked to the Items model and allows users to add the name of an item. The name
field is set to read-only once an item already exist.
"""
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


"""
Inline formset factory is used to handle creating multiple items in the inventory
list at the same time, and adding or editing items.

"""
ItemFormset = inlineformset_factory(
    Inventory,
    Items,
    form=ItemsForm,
    fields=['name'],
    extra=1,
    can_delete=False
)