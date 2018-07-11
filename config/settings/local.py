from .base import *  # noqa
from .base import env
import os
import logging

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', default=True)
AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY', default='YgeFf8iR3s46FGckkc4Du00Am9p6TFEGBGmyvyY2S7Vi9R1ugtKTc3akjcI6E7eA')
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1"
]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa F405

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'localhost'
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ['debug_toolbar']  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']


# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ['django_extensions']  # noqa F405

# Your stuff...
# ------------------------------------------------------------------------------

FB_APP_SECRET = env('FB_APP_SECRET')

LOG_PATH = os.path.join('/Users/jisuhan/Desktop/lisztfever/lisztfeverapp/', "log/")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s]- %(message)s'
        }
    },
    'handlers': {
        'django_error': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH + 'django.log',
            'formatter': 'standard'
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH + 'info.log',
            'formatter': 'standard'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'info': {
            'handlers': ['info', "console"],
            'level': 'DEBUG',
            'propagate': True
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['django_error', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        }
    },
}
