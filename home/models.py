from django.db import models

# Create your models here.

button_choices = (
    ('membership', 'Membership'),
    ('volunteering', 'Volunteering'),
    ('donation', 'Donation'),
)


def get_hero_slider_img_upload_path(instance, filename):
    # filename, ext = filename.split('.')
    return f'uploads/heroSlider/{filename}'


class HeroSlider(models.Model):
    main_text = models.CharField(max_length=255)
    sub_text = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=get_hero_slider_img_upload_path, blank=True, null=True)
    btn_to_show = models.CharField(
        choices=button_choices, max_length=50, verbose_name='Button to show')

    def __str__(self):
        return str(self.main_text)
