from app import app, db
from models import *

# Make sure you are in the app context
with app.app_context():
    # Drop all tables
    db.drop_all()

    # Recreate the tables
    db.create_all()
