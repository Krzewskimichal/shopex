from django.db import models
from django.contrib.auth.models import User

from shopex.settings import STATIC_URL


def upload_profile_image_path(instance, filename):
    return f'user_{instance.user.id}/profile_images/{filename}'


class ProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to=upload_profile_image_path)
    upload_at = models.DateTimeField(auto_now_add=True)
