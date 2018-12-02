import os
from app import create_app

# import config var from env
CONFIG_NAME = os.getenv('PROJECT_SETTINGS')

""" 
initialising flask app by calling create_app
and passing development config
"""
app = create_app(CONFIG_NAME)
