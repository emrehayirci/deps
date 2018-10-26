from django.contrib import admin
from .models import Post, Comment, DownVote, UpVote


admin.site.register(Post)
admin.site.register(Comment)
#admin.site.register(DownVote)
#admin.site.register(UpVote)
