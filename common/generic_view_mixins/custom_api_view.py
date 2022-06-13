"""
This module consists of Base API view to be used for class based requests to DjangoProd
"""
from rest_framework.exceptions import APIException
from common.enums.generic_enums import ResponseType
from rest_framework.views import APIView
from common.utilities import StructObj
from rest_framework import status



class CustomAPIView(APIView):
    ''' Base API view to be used in DjangoProd '''

    def validate_serializer(self, serializer, req_data, result_format=ResponseType.OBJ):
        ''' Validate serializer against request data '''
        req = serializer(data=req_data)
        if not req.is_valid():
            raise APIException(f"Please provide a valid request data", code=status.HTTP_400_BAD_REQUEST, errors=req.errors)
        return self.result_formatter(req.validated_data, result_format)

    
    def validate_many_serializer(self, serializer, req_data, result_format=ResponseType.OBJ):
        ''' Validate serializer against request data '''
        req = serializer(data=req_data, many=True)
        if not req.is_valid():
            raise APIException(f"Please provide a valid request data", code=status.HTTP_400_BAD_REQUEST, errors=req.errors)
        return self.result_formatter(req.validated_data, result_format)


    def result_formatter(self, result, format):
        ''' Format result '''
        if format == ResponseType.OBJ:
            return StructObj(result)
        return result
