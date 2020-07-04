from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    STATUS_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    type_user = models.CharField("Type User", max_length=100, choices=STATUS_CHOICES, default='seller')
    telephone = models.BigIntegerField("Phone", blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = """user data"""
        verbose_name_plural = """user data"""

