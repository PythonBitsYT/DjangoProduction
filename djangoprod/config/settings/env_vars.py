"""
This module consists of basic ENV configuration that will be use through
the project for reading values for .env.X file
"""
from djangoprod.config.settings_enums import MEDIA_STORAGE, STATIC_STORAGE
from .setup import *



###############################################################################################################
#############################################  ENV configurations #############################################
###############################################################################################################

############################################  Basic configurations ############################################
ENVIRONMENT=ENV('ENVIRONMENT')

#############################################  AWS configurations #############################################
AWS_ACCESS_KEY_ID = ENV('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = ENV('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = ENV('AWS_STORAGE_BUCKET_NAME')
AWS_STORAGE_BUCKET_REGION = ENV('AWS_STORAGE_BUCKET_REGION')
AWS_STATIC_STORAGE_BUCKET_NAME = ENV('AWS_STATIC_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_STATIC_DOMAIN = '%s.s3.amazonaws.com' % AWS_STATIC_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = STATIC_STORAGE
AWS_STATIC_LOCATION = STATIC_STORAGE
AWS_MEDIA_LOCATION = MEDIA_STORAGE

AWS_S3_FILE_OVERWRITE = False

#########################################  STATIC Data configurations #########################################
STATIC_ROOT = os.path.join( BASE_DIR, AWS_STATIC_LOCATION )
MEDIA_ROOT  =   os.path.join( BASE_DIR, AWS_MEDIA_LOCATION )

# This URL is useless, the actual static files URLs are generated using STATICFILES_STORAGE
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_STATIC_DOMAIN, AWS_STATIC_LOCATION)
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)

#! TODO-Boilerplate: Fix this name
STATICFILES_STORAGE = 'djangoprod.config.static_storage_backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'djangoprod.config.storage_media_backends.MediaStorage'
