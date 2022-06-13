from storages.backends.s3boto3 import S3Boto3Storage
from djangoprod.config.settings_enums import MEDIA_STORAGE

class MediaStorage(S3Boto3Storage):
    location = MEDIA_STORAGE
    file_overwrite = False