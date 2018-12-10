
from app.db.db_config import DbModel  # import db_config
import os
from app import create_app
from flask import current_app

# import development config var from env
CONFIG_NAME = os.getenv('PROJECT_SETTINGS')

"""
initialising flask app by calling create_app
and passing development config
"""
app = create_app(CONFIG_NAME)

# create db tables if not exists
db = DbModel(app)
db.create_tables()
