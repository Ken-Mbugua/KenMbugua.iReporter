from flask import Flask

# import blueprint from app/api/v1 __init__.py
from app.api.v1 import version_one as v1

# importing config dictionary from our config file
from instance.config import app_config, DevelopmentConfig

# from flask.ext.bcrypt import Bcrypt


def create_app(config_name):
    """
        create app function where app is initailased
    """
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_pyfile('../instance/config.py')
    app.config.from_object(app_config[config_name])
    #  # defining config instream
    # bcrypt = Bcrypt(app)
    print('CONFIG_CLASS', app_config[config_name])
    print('CONFIG_NAME: ', config_name)
    app.register_blueprint(v1)
    return app
