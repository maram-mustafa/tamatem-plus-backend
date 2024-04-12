from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **other_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(email, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name="Email Address", unique=True, blank=False, max_length=255
    )
    date_joined = models.DateTimeField(verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Date Of Last Login", auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name="User Account Active")
    is_staff = models.BooleanField(default=True, verbose_name="Staff Member")

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
