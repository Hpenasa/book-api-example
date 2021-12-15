from flask import  request, jsonify, Blueprint
from flask.json import jsonify



from database import books

books_bp = Blueprint('route-books', __name__)


@books_bp.route('/books', methods= ['POST'])
def add_book():
    ISBN = request.json['ISBN']
    title = request.json['title']
    author = request.json['author']
    price = request.json['price']

    data = (ISBN, title, author,price)
    book_id = books.insert_book(data)
    

    if book_id:
        book = books.select_book_by_id(book_id)
        return jsonify({'book' : book})
    return jsonify({'message': 'API  Error'})


@books_bp.route('/books', methods= ['GET'])
def get_books():
    data = books.select_all_books()
    if data:
        return jsonify({'books' : data})
    elif data == False:
        return jsonify({'message': 'API  Error'})
    else:
        return jsonify({'books' : {}})


@books_bp.route('/books', methods= ['PATCH'])
def patch_book():
    updated_book = {
            'isbn': request.json['isbn'],
            'title': request.json['title'],
            'author': request.json['author'] ,
            'price': request.json['price'] ,
            'id': request.args.get ('id')
    }
    
   
    if books.patch_books(updated_book):
        book = books.select_book_by_id(updated_book.get('id'))
        return jsonify(book)
    return jsonify({'message': 'patch  Error'})




@books_bp.route('/books', methods= ['PUT'])
def put_book():

    updated_book = {
        'isbn': request.json['isbn'],
        'title': request.json['title'],
        'author': request.json['author'] ,
        'price': request.json['price'] ,
        'id': request.args.get ('id')
    }

    if len(updated_book) == 0:
        return jsonify({'message': '400'})

    

    if books.update_book(updated_book):
        book = books.select_book_by_id(updated_book.get('id'))
        return jsonify(book)
    return jsonify({'message': 'PUT  Error'})


@books_bp.route('/books', methods= ['DELETE'])
def delete_books():
    id_arg = request.args.get('id')

    if books.delete_book(id_arg):
        return jsonify({'Message' : 'Book Deleted'})
    return jsonify({'message': 'API  Error'})


        
@books_bp.route('/')
def home():
    return '<h1>Book Store API!</h1>'

        