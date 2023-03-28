from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(models.Model):
    designation = (
        ('admin', 'Admin'),
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('peeker', 'Peeker')

    )

    id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=256, null=False)
    age = models.FloatField(max_length=256, null=True)
    email = models.EmailField(max_length=256, null=False, unique=True)
    password = models.CharField(max_length=256, null=False)
    address = models.CharField(max_length=256, null=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(auto_now=True)
    last_login = models.DateTimeField(default=timezone.now)
    designation = models.CharField(
        'designation of user who will come to our signup',
        max_length=32,
        default='peeker',
        choices=designation,
        null=False
    )

    def __str__(self) -> str:
        return f' user is {self.name} and {self.designation}'

    class Meta:
        ordering = ['last_login']
        db_table = 'user'
        verbose_name = "User"
        verbose_name_plural = "Users"
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__gte=18), name='user age check greater or equal 18')
        ]

