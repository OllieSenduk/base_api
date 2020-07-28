from django.db import models

# Needed libs to extend the user model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

# User manager class - helper functions for creating users & super users
# Used for


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """"Creates & saves a new user"""
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Customize the user model to support email instead of username"""
    email = models.EmailField(max_length=225, unique=True)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
