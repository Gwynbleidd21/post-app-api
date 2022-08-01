from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of the user API."""
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test for creating user successfully"""
        payload = {
            'user_id': '2',
            'password': 'test23'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(user_id=payload['user_id'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_id_exists_error(self):
        """Test for creating a duplicate user"""
        payload = {
            'user_id': '2',
            'password': 'test23'
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test for too short password"""
        payload = {
            'user_id': '2',
            'password': 'te'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            user_id=payload['user_id']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test for creating token"""
        user_details = {
            'user_id': '2',
            'password': 'reasfewf123'
        }
        create_user(**user_details)

        payload = {
            'user_id': user_details['user_id'],
            'password': user_details['password']
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_bad_cred(self):
        """Test for wrong credentials when creating token"""
        create_user(user_id='2', password='goodpass')
        payload = {
            'user_id': '3',
            'password': 'badpass'
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """Test for blank password"""
        payload = {
            'user_id': '3',
            'password': ''
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauth(self):
        """Test for getting unauthenticated user"""
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication."""

    def setUp(self):
        self.user = create_user(
            user_id='3',
            password='heslo123'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile(self):
        """Test for getting profile of authenticated user"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'user_id': self.user.user_id
        })

    def test_post_me_no_allowed(self):
        """Test POST is not allowed for the me endpoint."""
        res = self.client.post(ME_URL, {})

        self.assertEqual(
            res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )
