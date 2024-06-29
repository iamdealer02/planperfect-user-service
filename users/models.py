from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.db import models

class UserManager(DefaultUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Users(AbstractUser):
    username = None  # Removing the username field
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    # PASSWORD FIELD IS INHERITED FROM AbstractUser
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname']  # Email is the only required field; fname and lname are additional fields.

    objects = UserManager()  # Set the custom manager

    def __str__(self):
        return self.email
