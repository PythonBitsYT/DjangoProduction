"""
This module consists of decorator that is used to find and store client IP as request parameter
"""
from common.exceptions.custom_api_exception import CustomAPIException
from django.http import JsonResponse
from rest_framework import status


def set_client_ip(*args, **kwargs):
    """ Set client IP in request """
    def inner(request, *inner_args, **inner_kwargs):
        try:
            _client_ip = get_client_ip(request)
            if _client_ip is None:
                raise CustomAPIException("Client address cannot be none, please contact support")
            setattr(request, "_client_ip", _client_ip)
        except CustomAPIException as e:
            # Convert the RestAPIException response to JSON response
            return JsonResponse(e.__dict__["detail"], status=status.HTTP_409_CONFLICT)
        # Proceede with the url call
        return args[0](request, *inner_args, **inner_kwargs)
    return inner


def get_client_ip(request):
    """ Get IP of the client from request and store as request parameter """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
