"""
This module consists of basic test setups for django production project

NOTE: If these are failing you are probably missing something in the configurations.
Please refer to README.md in that case
"""
from django.test import TestCase
import platform


class Test_DjangoProd_Setup(TestCase):
    """ Test cases to verify django production project setup """

    def setUp(self):
        """ Perform basic setup """
        return super().setUp()


    def test_python_version(self):
        """ 
        Test if the python version used for setting up the project is correct 
        NOTE: You can change the version as per your requirements
        """
        self.assertEqual("3.9.9", platform.python_version())