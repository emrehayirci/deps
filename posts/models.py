from django.db import models
from django.contrib.auth.models import User as DjangoUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.DateTimeField()
    author = models.ForeignKey(DjangoUser)

class Comment:
    body = models.TextField()
    creation_date = models.DateTimeField()
    author = models.ForeignKey(DjangoUser)

class Upvote:
    author = models.ForeignKey(DjangoUser)
    item = models.ForeignKey(Post)

class Downvote:
    author = models.ForeignKey(DjangoUser)
    item = models.ForeignKey(Post)
