import re
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

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
    word_count = models.IntegerField(blank=True, default="")
    twitter_post = models.TextField(blank=True, default="")
    # use Choices as an iterable containing tuples
    # tuples: (value inserted into database, value rendered in the dropdown box
    status = models.CharField(max_length=20, choices=ARTICLE_STATUS, default="draft")
    # save current date time when model is created but wont change next time model is modified
    created_at = models.DateTimeField(auto_now_add=True)
    # save current date when model is updated
    updated_at = models.DateTimeField(auto_now=True)
    
    # related_name allows user.articles to load all article objects that user created
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")

    # override the built in save method
    def save(self, *args, **kwargs):
        # match and replace html tags with ""
        # replace newline characters with spaces
        text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))  # find words
        super().save(*args, **kwargs)
