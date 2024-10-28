from sre_constants import error

from flask import Blueprint, jsonify
from API.models.book_model import Book

fetch_book_blp = Blueprint("fetch_books", __name__)

class FetchBooks:
    @staticmethod
    @fetch_book_blp.route("/show", methods=["GET"])
    def fetch_all_books():
        return Book.query.all()

    @staticmethod
    @fetch_book_blp.route("/show/<id>", methods=["GET"])
    def fetch_book_by_id(id):
        result = Book.query.filter_by(id=id).first()
        if result:
            return jsonify(result.to_dict())
        else:
            return jsonify({"error" : "Book not found"}), 404