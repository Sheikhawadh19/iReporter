from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app

"""
export FLASK_APP="run.py"
export APP_SETTINGS="development"
export SECRET="a-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
export DATABASE_URL="postgresql://localhost/flask_api"

"""