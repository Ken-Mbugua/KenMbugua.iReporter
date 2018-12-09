
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

# create db tables if not exists


app = create_app(CONFIG_NAME)
db = DbModel()
db.create_tables()

# print("CURRENT_APP:::", current_app.config["DB_NAME"])
