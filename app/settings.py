from ._settings import *

# Add your custom settings here
LANGUAGE_CODE = 'ru'

INSTALLED_APPS += [
    'easy_thumbnails',
]

MEDIA_ROOT = BASE_DIR + '/media'
MEDIA_URL = '/media/'