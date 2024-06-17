from flask import Blueprint, request, jsonify
from extensions import db
from models.book import Book

book_bp = Blueprint('books', __name__, url_prefix='/books')

@book_bp.route('/', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@book_bp.route('/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

@book_bp.route('/', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        published_date=data['published_date'],
        isbn=data['isbn']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@book_bp.route('/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.title = data['title']
    book.author = data['author']
    book.published_date = data['published_date']
    book.isbn = data['isbn']
    db.session.commit()
    return jsonify(book.to_dict())

@book_bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

def to_dict(self):
    return {
        'id': self.id,
        'title': self.title,
        'author': self.author,
        'published_date': self.published_date.isoformat(),
        'isbn': self.isbn
    }

Book.to_dict = to_dict
