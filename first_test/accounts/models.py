from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


# Create your models here.
#https://www.youtube.com/watch?v=HshbjK1vDtY 23:00

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_admin=False, is_staff=False):
        if not email:
            raise ValueError("User must have an email adress")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)#change user password
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user



class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True) #can login
    staff = models.BooleanField(default=False)#staff non superuser
    admin = models.BooleanField(default=False)#superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff
