import os
from app import create_app

CONFIG = os.getenv('PROJECT_SETTINGS')

app = create_app()
