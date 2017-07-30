from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
# This project uses Django Authentication System
# For more information visit: https://docs.djangoproject.com/en/1.11/topics/auth/default/

#referenced from https://medium.com/@ramykhuffash/django-authentication-with-just-an-email-and-password-no-username-required-33e47976b517
class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)



EducationTypes = ((1, "Örgün öğretim"), (2, "İkinci Öğretim"), (3, "Yüksek Lisans"), (4, ("Doktora")))

class User(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=True, null=True)
    student_number = models.IntegerField(blank=True, null=True)
    faculty = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    grade = models.IntegerField(default=1, choices=EducationTypes)
    verified = models.BooleanField(default=False)

    #hooking up custom user manager
    objects = MyUserManager()

    #Used for making email sign ins instead of username
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
