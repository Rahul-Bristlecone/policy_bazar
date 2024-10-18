from flask import Flask
from .blueprints import register_blueprints
from BackEndAutomation.API.db_config import db


# application factory pattern or factory function - create_app()
# creating and configuring the instance of flask application (with or without db)
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:rsshrma92@localhost/rsshrma92'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)  # here, db is bound to the app
    register_blueprints(app)
    return app
