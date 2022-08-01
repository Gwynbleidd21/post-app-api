"""
Database models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager for users"""
    def create_user(self, user_id, password, **extra_fields):
        """Create, save and return new user"""
        if not user_id:
            raise ValueError('User needs a user id value')
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_id, password):
        """Create and return new superuser"""
        user = self.create_user(user_id, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in system"""
    user_id = models.CharField(default=True, unique=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'user_id'


class Prispevok(models.Model):
    """Prispevok in system"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255, blank=True)
    userId = models.IntegerField(default=True)

    def __str__(self):
        return self.title
