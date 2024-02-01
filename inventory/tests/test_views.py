from django.contrib.auth.models import User
from django.test import TestCase, Client
from inventory.models import Inventory, Items, Category

class TestInventoryView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user('testuser', 'm_tecle@hotmail.com', 'passwordtest')
        # Login test user
        self.client = Client()
        self.client.login(username='testuser', password='passwordtest')
        # Create a test category
        self.category = Category.objects.create(name="Category test")
        # Create a test inventory
        self.inventory = Inventory.objects.create(user=self.user, name="Inventory test", category=self.category)

    def test_create_inventory(self):
        response = self.client.post('/inventory/', {'name': 'New Inventory', 'category': self.category.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Inventory.objects.filter(name='New Inventory').exists())
