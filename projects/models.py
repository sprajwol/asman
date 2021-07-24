from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


def get_project_main_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    text = [
        character for character in instance.title if character.isalnum()]
    text = "".join(text)

    return f'uploads/projects/{text}/{text}_image.{ext}'


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    date = models.DateField()
    main_image = models.ImageField(
        upload_to=get_project_main_image_uploadpath, blank=True, null=True)
    location = models.CharField(max_length=50)
    category = models.ForeignKey(
        ProjectCategory, on_delete=models.SET_NULL, blank=True, null=True)
    summary = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return str(self.title)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Project.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('projectdetail', args=[str(self.slug)])
