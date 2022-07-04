"""
Init doctor for initializing settings

"""
from .setup import ENV

if ENV("ENVIRONMENT")=="PROD":
    from .core_prod import *
elif ENV("ENVIRONMENT")=="UAT":
    from .core_uat import *
else:
    from .core_dev import *