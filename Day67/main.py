from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = db.session.query(BlogPost).all()
    print(posts)
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/edit_post/<int:post_id>")
def edit_post(post_id):
    print("comes here"*100)
    print(post_id)
    header_text = "New Post" if post_id < 0 else "Edit Post"
    requested_post = None
    posts = db.session.query(BlogPost).all()
    print(posts)
    for blog_post in posts:
        if blog_post.id == post_id:
            requested_post = blog_post
    form = CreatePostForm()
    if form.validate_on_submit():
        # print(request.form['title'])
        # print(dt.datetime.now().strftime("%B %d, %Y"))
        # print(request.form['body'])
        new_post = BlogPost(
        title = request.form['title'],
        subtitle = request.form['subtitle'],
        date = dt.datetime.now().strftime("%B %d, %Y"),
        body = request.form['body'],
        author = request.form['author'],
        img_url = request.form['img_url']
        
            )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'),)
    else:
        return render_template("make-post.html", form=form, header_text=header_text)
    
@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        # print(request.form['title'])
        # print(dt.datetime.now().strftime("%B %d, %Y"))
        # print(request.form['body'])
        new_post = BlogPost(
    title = request.form['title'],
    subtitle = request.form['subtitle'],
    date = dt.datetime.now().strftime("%B %d, %Y"),
    body = request.form['body'],
    author = request.form['author'],
    img_url = request.form['img_url']
    
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'),)
    else:
        return render_template("make-post.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)