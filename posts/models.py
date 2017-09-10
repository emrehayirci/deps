from django.db import models
from profiles.models import User
from datetime import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    visible = models.BooleanField(default=True)
    author = models.ForeignKey(User)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    body = models.TextField()
    creation_date = models.DateTimeField()
    visible = models.BooleanField(default=True)
    author = models.ForeignKey(User)

class Upvote(models.Model):
    author = models.ForeignKey(User)
    item = models.ForeignKey(Post)

class Downvote(models.Model):
    author = models.ForeignKey(User)
    item = models.ForeignKey(Post)
