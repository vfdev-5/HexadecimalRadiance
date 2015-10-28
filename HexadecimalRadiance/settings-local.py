from settings import *

# http://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django
# USE python manage.py runserver --settings=CleanForest.settings-local to run server locally

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hexadicimal_radiance_db',
        'USER': 'vfdev',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost',
        'PORT': '',
    },
}