from flask import Flask
from flask_sqlalchemy import SQLAlchemy
dbAlchemy = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')
    dbAlchemy.init_app(app)

    with app.app_context():
        import toolkit.routes  # Import routes
        dbAlchemy.create_all()  # Create sql tables for our data models
        return app