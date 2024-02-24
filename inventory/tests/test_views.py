from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.db.utils import IntegrityError
from inventory.models import Inventory, Items, Category

"""
Use a database transaction so that if any part of the inventory
creation or inventory deletion fails, the changes will be rolled back
to prevent partial changes from affecting state of the database.
"""


class TestInventoryView(TestCase):
    def setUp(self):

        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='m_tecle@hotmail.com',
            password='passwordtest'
            )

        # Login test user
        self.client = Client()
        self.client.login(username='testuser', password='passwordtest')
        # Create a test category
        self.category = Category.objects.create(name="Category test")

        inventory_name = "Test Inventory"
        # Attempt to create a test inventory tied to the user and category
        try:
            with transaction.atomic():
                self.inventory = Inventory.objects.create(
                    name="Test Inventory",
                    category=self.category,
                    user=self.user
                    )
        except Exception as e:
            self.inventory = None

    """
    Create a new inventory through a post request
    After successful creation, checks for status code for redirection
    Checks that "New Inventory" was created and exists in the database
    """

    def test_create_inventory(self):
        response = self.client.post(
            '/inventory/',
            {'name': 'New Inventory',
             'category': self.category.id}
             )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Inventory.objects.filter(name='New Inventory').exists()
            )

    """
    Create a uniqe inventory specifically for this test
    Use the new inventory lists's pk for the deletion test
    Check that the inventory was deleted
    """

    def test_delete_list(self):
        try:
            with transaction.atomic():
                new_inventory = "Test inventory to delete"
                test_inventory = inventory = Inventory.objects.create(
                    name="Test inventory to delete",
                    category=self.category, user=self.user
                    )
                response = self.client.post(
                    f'/delete_list/{test_inventory.pk}/'
                    )
                self.assertEqual(response.status_code, 302)
                self.assertFalse(Inventory.objects.filter(
                    pk=test_inventory.pk).exists()
                    )
        except Exception as e:
            self.inventory = None

    """
    Called after each test to delete the test data from the database to
    avoid conflicts
    """

    def tearDown(self):
        User.objects.all().delete()
        Inventory.objects.all().delete()
        Category.objects.all().delete()
