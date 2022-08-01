"""
Tests for prispevok APIs.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Prispevok

# from prispevok.serializers import (
# PrispevokSerializer,
# PrispevokDetailSerializer
# )

PRISPEVOK_URL = reverse('prispevok:prispevok-list')


def detail_url(prispevok_id):
    """Create and return a prispevok detail URL."""
    return reverse('prispevok:prispevok-detail', args=[prispevok_id])


def create_prispevok(user, **params):
    """Create and return a sample prispevok."""
    defaults = {
        'title': 'Sample title',
        'body': 'Sample text'
    }
    defaults.update(params)
    prispevok = Prispevok.objects.create(user=user, **defaults)
    return prispevok


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicPrispevokAPITests(TestCase):
    """Test unauthenticated API requests."""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(PRISPEVOK_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePrispevokAPITests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(user_id='2', password='user123')
        self.client.force_authenticate(self.user)

    # def test_retrieve_prispevok(self):
    #     """Test retrieving a list of prispevoks."""
    #     create_prispevok(user=self.user)
    #     create_prispevok(user=self.user)
    #
    #     res = self.client.get(PRISPEVOK_URL)
    #
    #     prispevoks = Prispevok.objects.all().order_by('-id')
    #     serializer = PrispevokSerializer(prispevoks, many=True)
    #     self.assertEqual(res.data, serializer.data)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #
    # def test_prispevok_list_to_user(self):
    #     """Test list of prispevok is limited to authenticated user."""
    #     other_user = create_user(user_id='5', password='heslo5')
    #     create_prispevok(user=other_user)
    #     create_prispevok(user=self.user)
    #
    #     res = self.client.get(PRISPEVOK_URL)
    #     prispevoks = Prispevok.objects.filter(user=self.user)
    #     serializer = PrispevokSerializer(prispevoks, many=True)
    #     self.assertEqual(res.data, serializer.data)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #
    # def test_get_prispevok_detail(self):
    #     """Test get prispevok detail."""
    #     prispevok = create_prispevok(user=self.user)
    #
    #     url = detail_url(prispevok.id)
    #     res = self.client.get(url)
    #
    #     serializer = PrispevokDetailSerializer(prispevok)
    #     self.assertEqual(res.data, serializer.data)
    #
    # def test_create_prispevok(self):
    #     """Test creating a prispevok."""
    #     payload = {
    #         'title': 'sampl post',
    #         'body': 'boddy'
    #     }
    #     res = self.client.post(PRISPEVOK_URL, payload)
    #
    #     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    #     prispevok = Prispevok.objects.get(id=res.data['id'])
    #     for k, v in payload.items():
    #         self.assertEqual(getattr(prispevok, k), v)
    #     self.assertEqual(prispevok.user, self.user)
    #
    # def test_partial_update(self):
    #     """Test partial update of a prispevok."""
    #     original_body = 'telo'
    #     prispevok = create_prispevok(
    #     title='titul', user=self.user, body=original_body
    #     )
    #
    #     payload = {'title': 'new title'}
    #     url = detail_url(prispevok.id)
    #     res = self.client.patch(url, payload)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     prispevok.refresh_from_db()
    #     self.assertEqual(prispevok.title, payload['title'])
    #     self.assertEqual(prispevok.body, original_body)
    #     self.assertEqual(prispevok.user, self.user)
    #
    # def test_full_update(self):
    #     """Test full update of a prispevok."""
    #     prispevok = create_prispevok(
    #         user=self.user,
    #         title='title2',
    #         body='slobody',
    #     )
    #     payload = {
    #         'title': 'new title',
    #         'body': 'asdas'
    #     }
    #     url = detail_url(prispevok.id)
    #     res = self.client.put(url, payload)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     prispevok.refresh_from_db()
    #     for k, v in payload.items():
    #         self.assertEqual(getattr(prispevok, k), v)
    #     self.assertEqual(prispevok.user, self.user)
    #
    # def test_update_user_error(self):
    #     """Test changing the prispevok user results in an error."""
    #     new_user = create_user(user_id='7', password='2dasd')
    #     prispevok = create_prispevok(user=self.user)
    #
    #     payload = {'user': new_user.id}
    #     url = detail_url(prispevok.id)
    #     self.client.patch(url, payload)
    #     prispevok.refresh_from_db()
    #     self.assertEqual(prispevok.user, self.user)
    #
    # def test_delete_prispevok(self):
    #     """Test deleting a prispevok successful."""
    #     prispevok = create_prispevok(user=self.user)
    #     url = detail_url(prispevok.id)
    #     res = self.client.delete(url)
    #
    #     self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(Prispevok.objects.filter(id=prispevok.id).exists())

    # def test_prispevok_other_user_error(self):
    #     """Test trying to delete another users prispevok gives error."""
    #     new_user = create_user(user_id='9', password='2dasd')
    #     prispevok = create_prispevok(user=new_user)
    #
    #     url = detail_url(prispevok.id)
    #     res = self.client.delete(url)
    #
    #     self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
    #     self.assertTrue(Prispevok.objects.filter(id=prispevok.id).exists())
