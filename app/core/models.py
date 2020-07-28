from django.db import models

# Needed libs to extend the user model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

# User manager class - helper functions for creating users & super users


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """"Creates & saves a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
