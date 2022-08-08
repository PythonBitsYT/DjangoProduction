from rest_framework.exceptions import APIException
from django.utils.encoding import force_str
from rest_framework import status


class CustomAPIException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'A server error occurred.'
    default_code = 'NOT FOUND'
    default_name = "Conflict"

    def __init__(self, detail, status_code=status.HTTP_409_CONFLICT, name=None, code=0, field=None, errors=None):
        if detail is not None:
            self.detail = {'message': force_str(detail)}
        else:
            self.detail = {'message': force_str(self.default_detail)}

        self.detail['status'] = status_code or self.status_code
        self.detail['name'] = name or self.default_name
        self.detail['code'] = code
        self.detail['errors'] = errors
