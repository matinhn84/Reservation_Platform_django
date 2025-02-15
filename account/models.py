from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault(_("is_staff"), True)
        extra_fields.setdefault(_("is_superuser"), True)

        if not username:
            raise ValueError("Superuser must have a username.")

        return self.create_user(username, email, password, **extra_fields)



EXPERTISES = [
    ("dr", _("doctor")),
    ("sn", _("salon artist")),
    ("br", _("barber"))
]

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)  # Use this for login
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    expertise = models.CharField(_("expertise"), max_length=50, choices=EXPERTISES, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_premium = models.BooleanField(default=False)
    premium_until = models.DateTimeField(null=True, blank=True)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "username" 
    REQUIRED_FIELDS = ["email"]  

    def __str__(self):
        return self.username
    