"""
This module consits of generic enums used accross the project
"""
from enum import Enum


###################################################################################################
####################################### Enum Class ################################################
class ResponseType(Enum):
    """ Response type enum """
    DICT = "DICT" # Dictionary
    OBJ  = "OBJ" # Object
