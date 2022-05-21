from re import X
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
API_KEY = 'YOUR API KEY'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'RANDOM SECRET KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class AddMovieForm(FlaskForm):
    movie = StringField("Movie Title", validators=[DataRequired()])
    add_movie = SubmitField("Add Movie")

class MovieEditForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    done = SubmitField('Done')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), unique=False, nullable=False)
    rating = db.Column(db.Numeric, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(300), unique=False, nullable=False)
    
    def __repr__(self):
        return f'{self.title} {self.rating} {self.description}'

# new_movie = Movie(
# title="Phone Booth",
# year=2002,
# description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
# rating=7.3,
# ranking=10,
# review="My favourite character was the caller.",
# img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by('rating').all()
    x = len(all_movies)
    print(x)
    for movie in all_movies:
        movie.rating = float(movie.rating)
        movie.ranking = x
        x-=1
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    movie = Movie.query.get(id)
    form = MovieEditForm()
    
    if form.validate_on_submit():
        movie.rating = request.form['rating']
        movie.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home', code=302))
    else:
        return render_template("edit.html", movie=movie, form=form)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie = request.form['movie']
        req_params = {
            'api_key': API_KEY,
            'query': movie,
            'include_adult': False,
            'page': 1,
            
        }
        url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={movie}&page=1&include_adult=true'
        res = requests.get(url=url)
        movies = res.json()['results']
        print(movies)
        return render_template('select.html', movies=movies)
    else:
        return render_template("add.html", form=form)

@app.route("/select/<id>/<year>")
def select(id, year):
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}&language=en-US'
    res = requests.get(url=url)
    print(res.json())
    movie = res.json()
    movie['poster_path'] = 'https://image.tmdb.org/t/p/w500'+movie['poster_path']
    print(movie)
        
    new_movie = Movie(
    title=movie['original_title'],
    year=year,
    description=movie['overview'],
    rating=movie['vote_average'],
    ranking=0,
    review="My favourite character was the caller.",
    img_url=movie['poster_path']
    )
    db.session.add(new_movie)
    db.session.commit()
    # db_movie = Movie.query.filter_by(title=movie['original_title']).first()
    # return redirect(url_for('edit', id=db_movie.id), code=302)
    return redirect(url_for('home'), code=302)

@app.route("/delete/<id>", methods=["GET"])
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    
    return redirect(url_for('home'), code=302)
    



if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)