from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@email.com",
            password="pasword123"
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@email.com",
            password="pasword123",
            first_name="John",
            last_name="Smith"
        )

    def test_users_listed(self):
        """Tests that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # assert contains checks for :
        # http 200 requests
        # that the page contains the content
        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Tests that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Tests that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
