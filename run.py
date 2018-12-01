import os
from app import create_app

CONFIG = os.getenv('PROJECT_SETTINGS')
"""
main function run at run.py
"""
# grab env var from .env then passs it to app config_name = 'development'
config_name = os.getenv('PROJECT_SETTINGS')
app = create_app(config_name)
