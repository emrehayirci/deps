from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from profiles.views import register, login

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^register/', register, name="register"),
    url(r'^login/', login, name="login"),
    url(r'^users/', include('profiles.urls'))
]
