from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Test client to make requests to our api
from rest_framework.test import APIClient
# A module that contains status codes that show human readable responses
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(++params):
    return get_user_model().objects.create_user(++params)


class PublicUsersApiTest(TestCase):
    """Test the api endpoints that do not require auth"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating a user with valid payload is successful"""
        payload = (
            'email': 'user@test.com',
            'password': '12345678',
            'first_name': 'John',
            'last_name': 'Smith'
        )

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
