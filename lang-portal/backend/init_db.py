"""Initialize database with migrations and seed data."""
from flask_migrate import upgrade
from app import create_app, db
from seeds.initial_data import seed_data

def init_db():
    """Initialize database."""
    app = create_app()
    with app.app_context():
        # Run migrations
        upgrade()
        
        # Seed initial data
        seed_data()

if __name__ == '__main__':
    init_db()
