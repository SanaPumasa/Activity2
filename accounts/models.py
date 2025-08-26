from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_superuser=True):
        if not email:
            raise ValueError('Must have an email address')
        if not password:
            raise ValueError('Must have a password')

        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_superuser
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        return user

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active