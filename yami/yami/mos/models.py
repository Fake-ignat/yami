from django.db import models

# Create your models here.
class Person(models.Model):
    key = models.CharField(max_length=30, verbose_name='key')
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    date_birth = models.CharField(max_length=30, verbose_name='Date of Birth')
    expiration_date = models.CharField(max_length=30, verbose_name='Expiration Date')

    class Meta():
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'