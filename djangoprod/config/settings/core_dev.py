"""
#! TODO-Boilerplate: Fix this name
Settings for djangoprod project.

Base settings are imported from base_settings module
"""
from .base import *


###############################################################################################################
#############################################  Dev configurations #############################################
###############################################################################################################

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g537805d(=0=o*55t%b6(sn)8stzp!3y)u9t3^=+1(eo&qdqgv'

# This will later change to UI host only
ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

###########################################  Logging configurations ###########################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {'level': 'INFO', 'handlers': ['file']},
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ENV('LOG_DIR_PATH') + '/debug.log',
            'backupCount': 50, # keep at most 50 log files
            'maxBytes': 5242880, # 5*1024*1024 bytes (5MB)
            'formatter': 'app',
        },
        'console': { 
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'app',                                                         
        },  
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.filebased.EmailBackend',
        }
    },
    'loggers': {
        'common': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False
        },
    },
    'formatters': {
        'app': {
            'format': (
                u'%(asctime)s [%(levelname)-8s] '
                '(%(module)s.%(funcName)s) %(message)s'
            ),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
}



##############################################  DB configurations #############################################
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    # This picks a DB string from .env file
    # For SQLite use similar: DATABASE_URL=/////path/to/db/db.sqlite3
    'default': ENV.db(),
    
    # DB Read Replicas can be defined using
    'read_replica_1': ENV.db("DATABASE_READ_REPLICA_1_URL"),
    #'read_replica_2': ENV.db("DATABASE_READ_REPLICA_2_URL"),
}
