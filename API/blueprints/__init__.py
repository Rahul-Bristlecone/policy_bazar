from .add_book import AddBook
from .get_books import fetch_book_blp

# all blueprints are registered here
def register_blueprints(app):
    book_instance = AddBook()
    # fetch_instance = FetchBooks()
    app.register_blueprint(book_instance.add_book_blp)
    app.register_blueprint(fetch_book_blp)