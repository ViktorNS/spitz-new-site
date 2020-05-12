from django.conf import settings
from django.conf.urls.static import static

from ._urls import *

urlpatterns = [
    # place your patterns here

] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
