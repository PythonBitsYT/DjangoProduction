"""
This module consists of randomization utils
"""
import uuid



class RandomUtil(object):

    @classmethod
    def get_random_string(cls, len, upper_case):
        if upper_case:
            return uuid.uuid4().hex[:len].upper()
        else:
            return uuid.uuid4().hex[:len]

    @classmethod
    def get_random_id(cls):
        return uuid.uuid4().hex

    @classmethod
    def get_random_int(cls):
        return uuid.uuid4().int
