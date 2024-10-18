from BackEndAutomation.API.db_config import db


class Book(db.Model):
    __tablename__ = "Book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    author = db.Column(db.String(40), nullable=False)

    genre = db.Column(db.String(20), nullable=False)
