from storages.backends.s3boto3 import S3Boto3Storage
from djangoprod.config.settings_enums import STATIC_STORAGE
from django.conf import settings

class StaticStorage(S3Boto3Storage):
    location = STATIC_STORAGE
    bucket_name = settings.AWS_STATIC_STORAGE_BUCKET_NAME
    custom_domain = '%s.s3.amazonaws.com' % bucket_name
