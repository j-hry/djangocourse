from django.db import models
from django.contrib.auth.models import AbstractUser

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
)


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
    status = models.CharField(max_length=20, choices=ARTICLE_STATUS, default="draft")
    # save current date time when model is created but wont change next time model is modified
    created_at = models.DateTimeField(auto_now_add=True)
    # save current date when model is updated
    updated_at = models.DateTimeField(auto_now=True)
