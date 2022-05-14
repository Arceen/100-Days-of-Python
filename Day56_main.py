from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get('https://api.npoint.io/6ed5a6c737255c0801f6').json()
    return render_template("Day56_index.html", posts=posts)

@app.route('/post/<id>')
def post(id):
    posts = requests.get('https://api.npoint.io/6ed5a6c737255c0801f6').json()
    return render_template("Day56_post.html", post=posts[int(id)-1])

if __name__ == "__main__":
    app.run(debug=True)
