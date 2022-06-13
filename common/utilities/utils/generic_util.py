"""
This module consists of generic utils
"""
from urllib import parse
import urllib



class GenericUtil(object):

    @classmethod
    def get_dict_from_params(cls, query_params):
        query_dict = parse.parse_qs(query_params)
        return query_dict

    @classmethod
    def parse_query_to_dict(cls, url=None, query_params=None):
        if url:
            return dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))
        elif query_params:
            return dict(urllib.parse.parse_qsl(query_params))
