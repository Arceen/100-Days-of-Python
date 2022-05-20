from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# all_books = []

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Numeric, nullable=False)
    def __repr__(self):
        return f'{self.title} {self.rating} {self.author}'


@app.route('/')
def home():
    # global all_books
    # return render_template('index.html', books=all_books)
    all_books = db.session.query(Book).all()
    for book in all_books:
        book.rating = float(book.rating)
    return render_template('index.html', books=all_books)

@app.route('/edit/<id>', methods=["GET", "POST"])
def edit(id):
    book = Book.query.get(id)
    if request.method == 'POST':
        book.rating = float(request.form['rating'])
        db.session.commit()
        return redirect(url_for('home'), code=302)
    else:
        
        return render_template('edit.html', book=book)

@app.route('/delete/<id>')
def delete(id):
    db.session.delete(Book.query.get(id))
    db.session.commit()
    return redirect(url_for('home'), code=302)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=='POST':
        # d = request.form.to_dict().copy()
        # d['rating'] = int(d['rating'])
        # all_books.append(d)
        # print(all_books)
        b = request.form.to_dict()
        book = Book(title=b['title'], author=b['author'], rating=float(b['rating']))
        db.session.add(book)
        db.session.commit()
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
