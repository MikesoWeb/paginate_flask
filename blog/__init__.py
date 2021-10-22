import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = os.urandom(36)
    db.init_app(app)

    from blog.main.routes import main

    app.register_blueprint(main)

    return app
