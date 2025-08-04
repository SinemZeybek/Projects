from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Scss(app, static_dir='static', asset_dir='static/scss')

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        from .models import MyTask
        db.create_all()

    return app
