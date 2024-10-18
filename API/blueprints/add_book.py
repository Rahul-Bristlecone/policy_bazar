from flask import Blueprint
from BackEndAutomation.API.models import book_model

# logic and code implementation of add book feature
class AddBook:
    def __init__(self):
        self.add_book_blp = Blueprint('add_book', __name__)
        self.create_book()

    def create_book(self):
        @self.add_book_blp.route('/book', methods=['POST'])
        def add_book():
            """
            when the endpoint "/book" is hit,
            then all the data from book_table should come as response in the form of json
            """
            return "Book added"
