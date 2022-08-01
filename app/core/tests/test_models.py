"""
Test models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_id(self):
        user_id = '2'
        password = '123'
        user = get_user_model().objects.create_user(
            user_id=user_id,
            password=password
        )

        self.assertEqual(user.user_id, user_id)
        self.assertTrue(user.check_password(password))

    def test_new_user_without_id_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            '1',
            '1234'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_prispevok(self):
        user = get_user_model().objects.create_user(
            '2',
            'test123'
        )
        prispevok = models.Prispevok.objects.create(
            user=user,
            title='My death',
            body='I die'
        )

        self.assertEqual(str(prispevok), prispevok.title)
