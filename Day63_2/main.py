# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(20) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
# db.commit()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f'{self.title} {self.rating} {self.author}'

# book = Book.query.filter_by(title="Harry Potter").first()
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book.title = "Harry Potter: Order of Phoenix"
# db.session.commit()
# books = db.session.query(Book).all()
# print(books)
book_id = 1
book = Book.query.get(book_id)
db.session.delete(book)
db.session.commit()

