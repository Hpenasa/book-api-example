
from flask import Flask
from flask.json import jsonify

from database import books, setup
from resources.books import books_bp

app = Flask(__name__)
setup.create_tables()
app.register_blueprint(books_bp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True) 


