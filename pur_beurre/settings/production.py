from. import *

ALLOWED_HOSTS = ["161.35.123.169", "indiana-p10.pythonclassmates.org", "localhost", "127.0.0.1"]
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
