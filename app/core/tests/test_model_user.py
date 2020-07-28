from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

    def test_create_user_with_email_valid(self):
        """Test creating new user with email works"""
        email = "test@test.com"
        password = "secret"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_new_user_email_normalized_valid(self):
        """Test that the email is normalized"""
        email = "test@TEST.com"
        password = "secret"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """Test email errors"""
        User = get_user_model()

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_new_user_username_invalid(self):
        email = "test@test.com"
        password = "secret"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass

    def test_create_super_user_valid(self):
        email = "admin@test.com"
        password = "secret"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)
