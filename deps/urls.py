from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from api.profiles.views import register, login
from api.posts.views import CommentViewSet, PostViewSet
from rest_framework import routers, views

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^posts/', include('api.posts.urls')),
    url(r'^register/', register, name="register"),
    url(r'^login/', login, name="login"),
    url(r'^users/', include('api.profiles.urls')),
    url(r'^', TemplateView.as_view(template_name="index.html"))
]


