from django.db import models
from django.db.models import Value as V
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=200, unique=True, verbose_name='Email')
    username = models.CharField(max_length=200, unique=True, verbose_name='User name')
    first_name = models.CharField(max_length=200, unique=False, verbose_name='First name')
    last_name = models.CharField(max_length=200, unique=False, verbose_name='Last name')

class CSV_data(models.Model):
    fullname = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name='User')
    job = models.CharField(max_length=200, verbose_name='Job')
    email_csv = models.EmailField(max_length=200, unique=True, verbose_name='Email')
    domain_name = models.CharField(max_length=200, verbose_name='Domain name')
    phone_number = models.CharField(max_length=200, verbose_name='Phone number')
    company_name = models.CharField(max_length=200, verbose_name='Company name')
    text = models.CharField(max_length=1000, verbose_name='Text')
    integer = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)], verbose_name='Integer')
    address = models.CharField(max_length=200, verbose_name='Address')
    data = models.DateTimeField(default=timezone.now, verbose_name='Data')





