from django.conf.urls import url
from .views import details, index

urlpatterns = [
    url(r'^(?P<post_id>[0-9])/$', details),
    url(r'^$', index, name='home')

]
