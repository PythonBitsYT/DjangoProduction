"""
This module consists of validations related util
"""
import re



class ValidationUtil(object):

    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    @classmethod
    def getEmailRegex(cls, email):
        if cls.EMAIL_REGEX.match(email):
            return True
        else:
            return False

    @classmethod
    def validMobileNumberPattern(cls):
        return r'^[5-9]\d{9,10}$'
