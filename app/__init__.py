from flask import Flask

# import blueprints from v1 __init__
from app.api.v1 import version_one as v1


def create_app():
    """
        create app function where app is initailased
    """
    app = Flask(__name__)
    app.register_blueprint(v1)
    return app
