from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    """An address the user wants to store and retrieve"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    street_address = models.TextField()
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self):
        """Return a string representation of the model."""
        return '{}, {}'.format(self.last_name, self.first_name)
