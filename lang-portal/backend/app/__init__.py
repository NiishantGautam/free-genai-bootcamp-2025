"""Flask application factory."""
from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    """Create Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize API
    api = Api(app)

    # Register blueprints
    from app.api.dashboard import blp as dashboard_blp
    from app.api.words import blp as words_blp
    from app.api.study import blp as study_blp

    api.register_blueprint(dashboard_blp)
    api.register_blueprint(words_blp)
    api.register_blueprint(study_blp)

    return app
