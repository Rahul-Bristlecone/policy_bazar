from flask import Blueprint
from BackEndAutomation.API.models.book_model import Book

fetch_book_blp = Blueprint("fetch_books", __name__)

class FetchBooks:
    def __init__(self):
        self.fetch_all_books()

    @staticmethod
    @fetch_book_blp.route("/show", methods=["GET"])
    def fetch_all_books():
        return Book.query.all()