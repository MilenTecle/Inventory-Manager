from django.contrib.auth.models import User
from django.test import TestCase, Client
from inventory.models import Inventory, Items, Category

class TestInventoryView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user (
            username='testuser',
            email='m_tecle@hotmail.com',
            password='passwordtest'
            )
        # Login test user
        self.client = Client()
        self.client.login(username='testuser', password='passwordtest')
        # Create a test category
        self.category = Category.objects.create(name="Category test")

        # Create a new inventory through a post request
        # After successful creation, checks for status code for redirection
        # Checks that "New Inventory" was created and exists in the database
    def test_create_inventory(self):
        response = self.client.post('/inventory/', {'name': 'New Inventory', 'category': self.category.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Inventory.objects.filter(name='New Inventory').exists())


        # Called after each test to delete the test data from the database to avoid conflicts
    def tearDown(self):
        User.objects.all().delete()
        Inventory.objects.all().delete()
        Category.objects.all().delete()
