import os
from app import create_app

CONFIG = os.getenv('PROJECT_SETTINGS')
"""
main function run at run.py
"""
app = create_app()
