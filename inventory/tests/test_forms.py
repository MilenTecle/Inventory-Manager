from django.test import TestCase
from inventory.forms import InventoryForm, ItemsForm


# Inventoryform test for valid submission
class InventoryFormTest(TestCase):
    def test_inventory_form_valid(self):
        data = {'name': 'Box 1', 'category': 'Closet'}
        form = InventoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Inventoryform test for invalid submission
    def test_inventory_form_valid(self):
        data = {}
        form = InventoryForm(data=data)
        self.assertFalse(form.is_valid())


# ItemsForms test for valid submission
class ItemsFormTest(TestCase):
    def test_items_form_valid(self):
        data = {'name': 'Item'}
        form = InventoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    # ItemsForms test for invalid submission
    def test_items_form_valid(self):
        data = {}
        form = InventoryForm(data=data)
        self.assertFalse(form.is_valid())
