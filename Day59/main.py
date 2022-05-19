from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
    posts = requests.get('https://api.npoint.io/6ed5a6c737255c0801f6').json()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    header_text = "Contact Me"
    if request.method == 'POST':
        header_text = 'Successfully sent message'
    return render_template('contact.html', header_text=header_text)


if __name__ == '__main__': 
    app.run(debug=True)