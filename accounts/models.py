from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    gender_choices = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'None'),
        ('U', 'Unset')
    ]

    address = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(choices=gender_choices, default='U', max_length=2)
    phone = models.CharField(blank=True, max_length=15, null=True)

    @property
    def is_author(self):
        return hasattr(self, 'author')

    def __str__(self):
        return self.username
