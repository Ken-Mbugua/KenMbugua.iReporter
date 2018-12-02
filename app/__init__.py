from flask import Flask

# import blueprint from app/api/v1 __init__.py
from app.api.v1 import version_one as v1

# importing config dictionary from our config file
from instance.config import app_config


def create_app(config_name):
    """
        create app function where app is initailased
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])  # defining config instream
    # app.config.from_pyfile('instance/config.py')

    app.register_blueprint(v1)
    return app
