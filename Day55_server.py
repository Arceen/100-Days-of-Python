from flask import Flask, render_template, url_for
app = Flask(__name__)
@app.route('/')
def hello():
    # return '<h1>Hello World!</h1>'
    return render_template('Day55_index.html')

if __name__ == "__main__":
    app.run(debug=True) 
