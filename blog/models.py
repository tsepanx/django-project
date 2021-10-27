from django.contrib.auth.models import AbstractUser
from django.db import models

from app import settings


class CustomUser(AbstractUser):
    pass


class Article(models.Model):
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author = models.ForeignKey(
        # django.contrib.auth.get_user_model()
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    pub_date = models.DateTimeField('Date published')
    text = models.CharField(max_length=10 ** 4)
