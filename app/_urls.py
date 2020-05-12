# generated: 22d885fd7919f75645d9d6c8f51e64ad

from django.conf.urls import url, include
from django.contrib import admin

import dog.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(dog.urls)),
]