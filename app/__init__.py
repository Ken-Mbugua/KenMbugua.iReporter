from flask import Flask

# import blueprints from v1 __init__
from app.api.v1 import version_one as v1

# import config dict from config file instance/config
from instance.config import app_config


def create_app(config_name):
    """
        create app function where app is initailased
    """
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])  # defining config instream
    app.config.from_pyfile('config.py')

    app.register_blueprint(v1)
    return app
