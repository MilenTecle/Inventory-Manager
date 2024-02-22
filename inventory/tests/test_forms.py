from django.test import TestCase
from django.contrib.auth.models import User
from inventory.models import Category
from inventory.forms import InventoryForm, ItemsForm


# Inventoryform test for valid submission
class InventoryFormTest(TestCase):
    def setUp(self):
        # Create a user for the test
        self.user = User.objects.create_user(
            username='testuser',
            password='password')
        # Create a category for the test
        self.category = Category.objects.create(
            name='Test Category',
            user=self.user)

    def test_inventory_form_valid(self):
        data = {'name': 'Box 1', 'category': self.category.id}
        form = InventoryForm(data=data, user=self.user)
        self.assertTrue(form.is_valid())

    # Inventoryform test for invalid submission
    def test_inventory_form_invalid(self):
        data = {}
        form = InventoryForm(data=data, user=self.user)
        self.assertFalse(form.is_valid())


# ItemsForms test for valid submission
class ItemsFormTest(TestCase):
    def test_items_form_valid(self):
        data = {'name': 'Item'}
        form = ItemsForm(data=data)
        self.assertTrue(form.is_valid())

    # ItemsForms test for invalid submission
    def test_items_form_invalid(self):
        data = {}
        form = ItemsForm(data=data)
        self.assertFalse(form.is_valid())
