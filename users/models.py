from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=150, blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True, null=True)

