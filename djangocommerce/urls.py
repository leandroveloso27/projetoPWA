
from django.conf.urls import url
from django.contrib import admin
from core.views import index, product

urlpatterns = [
    url(r'^$', index),
    url(r'^$', product),
    url(r'^admin/', admin.site.urls),
]
