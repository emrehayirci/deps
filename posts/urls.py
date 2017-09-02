from django.conf.urls import url
from .views import details, index, create_post, create_comment, remove_comment

urlpatterns = [
    url(r'^(?P<post_id>[0-9])/comments/(?P<comment_id>[0-9])/$', remove_comment),
    url(r'^(?P<post_id>[0-9])/comments/$', create_comment),
    url(r'^(?P<post_id>[0-9])/$', details),
    url(r'^new/$', create_post, name='new_post'),
    url(r'^$', index, name='home'),

]
