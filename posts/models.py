from django.db import models
from profiles.models import User
from datetime import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, models.SET_NULL, null=True)
    body = models.TextField()
    creation_date = models.DateTimeField()
    visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True)

class Upvote(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    item = models.ForeignKey(Post, models.SET_NULL, null=True)

class Downvote(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    item = models.ForeignKey(Post, models.SET_NULL, null=True)
