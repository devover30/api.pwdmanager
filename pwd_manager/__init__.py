from flask import Flask
from .extensions import db
from views.search import search_blueprint
from views.addUser import addUser_blueprint
from views.admin import admin_blueprint
from views.getAll import getall_blueprint

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    app.register_blueprint(getall_blueprint)
    app.register_blueprint(search_blueprint)
    app.register_blueprint(addUser_blueprint)
    app.register_blueprint(admin_blueprint)

    db.init_app(app)

    return app

