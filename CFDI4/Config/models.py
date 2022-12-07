from django.db import models
from django.contrib.auth.models import User
from Profiles.models import user_avatar_directory_path
class CSSConf(models.Model):
    user = models.ForeignKey(User, related_name='user_confCSS', on_delete=models.CASCADE)
    fondo = models.ImageField(upload_to=user_avatar_directory_path)
    backColor = models.CharField(max_length=6, blank=True)
    