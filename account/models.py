from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        # self.model == User
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db) 
        return user

    def create_user(self, email, password, **kwargs):
        return self._create(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        return self._create(email, password, **kwargs)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

>>>>>>> 48c7e75a09164b0f1789eaa12026bd1e5903f703
