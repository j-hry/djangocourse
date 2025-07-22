from django.db import models
from django.contrib.auth.models import AbstractUser


# use the built in user model from the auth app
class UserProfile(AbstractUser):
    pass


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")  # default is normally None
    word_count = models.IntegerField()
    twitter_post = models.TextField(blank=True, default="")
    # use Choices as an iterable containing tuples
    # tuples: (value inserted into database, value rendered in the dropdown box
    status = models.CharField(
        max_length=20,
        choices=(
            ("draft", "draft"),
            ("inprogress", "in progress"),
            ("published", "published"),
        ),
    )
