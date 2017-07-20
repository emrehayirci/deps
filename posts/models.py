from django.db import models
from profiles.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.DateTimeField()
    author = models.ForeignKey(User)

class Comment:
    body = models.TextField()
    creation_date = models.DateTimeField()
    author = models.ForeignKey(User)

class Upvote:
    author = models.ForeignKey(User)
    item = models.ForeignKey(Post)

class Downvote:
    author = models.ForeignKey(User)
    item = models.ForeignKey(Post)
