from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            user_id=2,
            password='heslo123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            user_id=3,
            password="heesloo2"
        )

    def test_users_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.user_id)

    # def test_edit_user_page(self):
    #     url = reverse('admin:core_user_change', args=[self.user.id])
    #     res = self.client.get(url)
    #
    #     self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
