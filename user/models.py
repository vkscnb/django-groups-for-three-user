from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.db import models

from . import managers


class User(AbstractUser):
    """
    A User model that uses `email` as it's default identifier instead of
    username.
    """
    # class Types(models.TextChoices):
    #     DEFAULT = '', ''
    #     TEACHER = "Teacher", "Teacher"
    #     STUDENT = "Student", "Student"

    # base_type = Types.DEFAULT
    type = models.CharField(
        max_length=50, 
        choices=(
            ("Teacher", "Teacher"),
            ("Student", "Student")
        ),
        null=True,
    )

    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, null=True)
    gender = models.CharField(
        max_length=20,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
    )
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.UserManager()

    def __str__(self):
        return self.email

# def save(self, *args, **kwargs):
#     self.password = make_password(self.password)
#     super(User, self).save(*args, **kwargs)
