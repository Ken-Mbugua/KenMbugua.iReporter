from flask import Flask

# import blueprint from app/api/v1 __init__.py
from app.api.v1 import version_one as v1
from app.api.v2 import version_two as v2

# importing config dictionary from our config file
from instance.config import app_config


def create_app(config_name):
    """
        create app function where app is initailased
    """
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_pyfile('../instance/config.py')

    # defining config instream
    app.config.from_object(app_config[config_name])

    print('CONFIG_CLASS', app_config[config_name])
    print('CONFIG_NAME: ', config_name)
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app
