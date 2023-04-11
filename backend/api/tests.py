import json
from django.test import Client, TestCase
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import include, path, reverse
from rest_framework import status
from backend.api.serializers import *

from backend.main.models import Account
# Create your tests here.

client = Client()

class GetAllAccountTest(TestCase):
    """ Test module for GET all accounts API """

    def setUp(self):
        Account.objects.create(
            name='Casper', username='Casper', email='casper@gmail.com', is_prosumer=True)
        Account.objects.create(
            name='Ben', username=1, email='ben@gmail.com', is_prosumer=False)
        Account.objects.create(
            name='John', username=2, email='john@gmail.com', is_prosumer=True)
        Account.objects.create(
            name='Bob', username=6, email='bob@gmail.com', is_prosumer=False)

    def test_get_all_accounts(self):
        # get API response
        response = client.get(reverse('accounts'))
        # get data from db
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleAccountTest(TestCase):
    """ Test module for GET single Account API """

    def setUp(self):
        self.casper = Account.objects.create(
            name='Casper', username='Casper', email='casper@gmail.com', is_prosumer=True)
        self.Ben = Account.objects.create(
            name='Ben', username=1, email='ben@gmail.com', is_prosumer=False)
        self.John = Account.objects.create(
            name='John', username=2, email='john@gmail.com', is_prosumer=True)
        self.Bob = Account.objects.create(
            name='Bob', username=6, email='bob@gmail.com', is_prosumer=False)

    def test_get_valid_single_Account(self):
        response = client.get(
            reverse('account', kwargs={'pk': self.John.pk}))
        account = Account.objects.get(pk=self.John.pk)
        serializer = AccountSerializer(account)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_Account(self):
        response = client.get(
            reverse('account', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewAccountTest(TestCase):
    """ Test module for inserting a new Account """

    def setUp(self):
        self.valid_payload = {
            'name': 'Ben',
            'username': 'Ben 2',
            'email': 'ben2@gmail.com',
            'is_prosumer': True
        }
        self.invalid_payload = {
            'name': '',
            'username': 4,
            'email': 'Pamerion',
            'is_prosumer': 'White'
        }

    def test_create_valid_Account(self):
        response = client.post(
            reverse('updateAccount'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_Account(self):
        response = client.post(
            reverse('updateAccount'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleAccountTest(TestCase):
    """ Test module for updating an existing Account record """

    def setUp(self):
        self.casper = Account.objects.create(
            name='Casper', username='Casper', email='casper@gmail.com', is_prosumer=True)
        self.Ben = Account.objects.create(
            name='Sam', username='Sam', email='sam@gmail.com', is_prosumer=False)
        self.valid_payload = {
            'name': 'Ben',
            'username': 'Ben',
            'email': 'ben@gmail.com',
            'is_prosumer': True
        }
        self.invalid_payload = {
            'name': '',
            'username': 4,
            'email': 'Pamerion',
            'is_prosumer': False
        }

    def test_valid_update_Account(self):
        response = client.put(
            reverse('updateAccount', kwargs={'pk': self.Ben.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_Account(self):
        response = client.put(
            reverse('updateAccount', kwargs={'pk': self.Ben.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleAccountTest(TestCase):
    """ Test module for deleting an existing Account record """

    def setUp(self):
        self.casper = Account.objects.create(
            name='Casper', username='Casper', email='casper@gmail.com', is_prosumer=True)
        self.Ben = Account.objects.create(
            name='Ben', username='Ben', email='ben@gmail.com', is_prosumer=False)

    def test_valid_delete_Account(self):
        response = client.delete(
            reverse('deleteAccount', kwargs={'pk': self.Ben.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_Account(self):
        response = client.delete(
            reverse('deleteAccount', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)