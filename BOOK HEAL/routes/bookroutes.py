from flask import Blueprint
from controllers import bookcontroller

book_bp = Blueprint("BookBP", __name__, url_prefix="/Books")
@book_bp.route("/add", methods=["POST"])
def createBook():
    return bookcontroller.createBook()