from django.conf.urls import url
from .views import details, index, create_post

urlpatterns = [
    url(r'^(?P<post_id>[0-9])/$', details),
    url(r'^new/$', create_post, name='new_post'),
    url(r'^$', index, name='home')

]
