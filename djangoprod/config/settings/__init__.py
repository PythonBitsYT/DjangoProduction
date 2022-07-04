"""
Init doctor for initializing settings

"""
from .setup import ENV

if ENV("ENVIRONMENT")=="STAGE1":
    pass
else:
    from .core_dev import *