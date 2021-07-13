from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(
        max_length=100, verbose_name='Applicant Full Name')
    email = models.EmailField(max_length=100, verbose_name='Email Address')
    mobile_number_regex = RegexValidator(
        regex=r'(?:\+977[- ]?)?(98\d{8}|97\d{8}|96\d{8})$', message="Phone number must be entered in the format: '(?:\+977[- ]?)?(98\d{8}|97\d{8}|96\d{8})'. Up to 15 digits allowed.")
    mobile_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Mobile Number')
    address = models.CharField(max_length=100, verbose_name='Address')
    message = models.TextField()

    def __str__(self):
        return str(self.full_name)
