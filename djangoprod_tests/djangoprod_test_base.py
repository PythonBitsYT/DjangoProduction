"""
Base class for all the test cases in DjangoProd
"""
from django.test import TestCase


class dprod_http_methods(object):
    """ DjangoProd base HTTP methods """

    def post(self):
        """ Not implemented """
        raise NotImplementedError

    def get(self):
        """ Not implemented """
        raise NotImplementedError


class DjangoProdTestBase(TestCase):
    """ Base class for all the test cases in DjangoProd """

    def setUp(self):
        """ Setup HTTP methods for DjangoProd """
        self.dprod = dprod_http_methods()
        self.dprod.post = self.post
        self.dprod.get = self.get
        super().setUp()

    def post(self, path, data=None, **kwargs):
        """ DjangoProd Post method """
        return self.client.post(path, data=data, content_type="application/json", **kwargs)


    def get(self, path, data=None, **kwargs):
        """ DjangoProd Get method """
        return self.client.get(path, data=data, content_type="application/json", **kwargs)