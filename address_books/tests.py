from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Address


def create_test_address():

    address = {
        'first_name': 'Guido',
        'last_name': 'Van Rossum',
        'phone_number': '555-555-5555',
        'email_address': 'guido@dropbox.com',
        'street_address': '2323 Elderberry Lane\nCamelot, CA 55555',
        # 'owner': 1
    }
    new_address = Address(**address)
    # new_address.save()
    return new_address


# Create your tests here.

class AddressModelTests(TestCase):
    """Test of Address model"""

    def test_add_address(self):
        """Test database model."""
        new_address = create_test_address()
        self.assertEqual(new_address.first_name, 'Guido')

class IndexPageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'address_books/index.html')

class AddressesPageTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', password='top_secret')

    def test_uses_addresses_template(self):
        self.client.login(username='jacob', password='top_secret')
        response = self.client.get('/addresses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'address_books/addresses.html')

class AddressPageTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', password='top_secret')
        current_address = create_test_address()

    def test_uses_address_template(self):
        self.client.login(username='jacob', password='top_secret')
        response = self.client.get('/address/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'address_books/address.html')

class EditAddressPageTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', password='top_secret')

    def test_uses_edit_address_template(self):
        self.client.login(username='jacob', password='top_secret')
        response = self.client.get('/edit_address/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'address_books/edit_address.html')

class NewAddressPageTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', password='top_secret')

    def test_uses_new_address_template(self):
        self.client.login(username='jacob', password='top_secret')
        response = self.client.get('/new_address/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'address_books/new_address.html')
