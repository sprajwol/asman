from django.db import models

# Create your models here.


def get_image_upload_path(instance, filename):
    album_name = instance.photo_album
    print("album_name", album_name)

    return f'uploads/gallery/{album_name}/{filename}'


class Album(models.Model):
    photo_album_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.photo_album_name)


class Image(models.Model):
    image = models.ImageField(
        upload_to=get_image_upload_path)
    photo_album = models.ForeignKey(
        Album, on_delete=models.CASCADE, default="others", related_name="images")

    def __str__(self):
        return str(self.image)
