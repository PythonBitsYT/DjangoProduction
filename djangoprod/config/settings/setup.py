"""
This module is the root setup for the complete django project
"""
from pathlib import Path
import environ
import sys
import os



# Setup paths for the project
ROOT_DIR  = Path(__file__).resolve().parent.parent.parent.parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(BASE_DIR)

# Setup ENV for the project
ENV = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Take environment variables from .env file
environ.Env.read_env(env_file=os.path.join(ROOT_DIR, '.env')) # reading .env file
