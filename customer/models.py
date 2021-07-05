from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomerModel(AbstractUser):
    avatar=models.ImageField(upload_to='avatar')
    class Meta:
        db_table='İstifadəçilər'
        verbose_name='Istifadeçi'
        verbose_name_plural='İstifadəçilər'
    def __str__(self):
        return self.username