from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
# Create your models here.


def get_member_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    full_name = [
        character for character in instance.full_name if character.isalnum()]
    full_name = "".join(full_name)

    return f'uploads/about/members/{instance.full_name}/{instance.full_name}_image.{ext}'


def get_customer_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    full_name = [
        character for character in instance.full_name if character.isalnum()]
    full_name = "".join(full_name)

    return f'uploads/about/testimonials/{instance.full_name}/{instance.full_name}_image.{ext}'


class Member(models.Model):
    full_name = models.CharField(
        max_length=100, verbose_name='Member Full Name')
    image = models.ImageField(upload_to=get_member_image_uploadpath,
                              blank=True, null=True, verbose_name='Member Image')
    position = models.CharField(max_length=50)
    display_rank = models.PositiveIntegerField(
        blank=True, null=True, validators=[MinValueValidator(1)])
    mobile_number_regex = RegexValidator(
        regex=r'(?:\+977[- ]?)?(98\d{8}|97\d{8}|96\d{8})$', message="Phone number must be entered in the format: '(?:\+977[- ]?)?(98\d{8}|97\d{8}|96\d{8})'. Up to 15 digits allowed.")
    mobile_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Mobile Number')
    email = models.EmailField(
        max_length=100, blank=True, null=True, verbose_name='Email Address')
    msg = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return str(self.full_name)

    class Meta:
        ordering = ('display_rank',)


class Testimonial(models.Model):
    full_name = models.CharField(
        max_length=100, verbose_name='Reviewer Full Name')
    image = models.ImageField(upload_to=get_customer_image_uploadpath,
                              blank=True, null=True, verbose_name='Image')
    organization = models.CharField(
        max_length=100, verbose_name='Reviewer Organization Name')
    position = models.CharField(
        max_length=50, verbose_name='Reviewer Position')
    testimonial = models.TextField()
    created_at = models.DateField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return str(self.full_name)

# class DonationDistribution(models.Model):
