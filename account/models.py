from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        not_selected = 'not_selected', "Not Selected",
        male = 'male', 'Male',
        female = 'female', 'Female'

    gender = models.CharField(max_length=30, choices=GenderChoices.choices, default=GenderChoices.not_selected)
    profile_image = models.ImageField(upload_to='images/Profiles', blank=True, null=True)

    def __str__(self):
        return self.get_username()
