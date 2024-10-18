# setup.py
from BackEndAutomation.API import create_app
from BackEndAutomation.API.db_config import db
from BackEndAutomation.API.models.book_model import Book


# Import your models here
app = create_app()

with app.app_context():
    db.create_all()  # Create tables
    # Example CRUD operations
    db.session.commit()
