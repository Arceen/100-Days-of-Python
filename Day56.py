from django.shortcuts import render
from flask import Flask, render_template
import datetime as dt
import random
import requests
import json
app = Flask(__name__)


@app.route('/')
def home():
    v = random.randint(0,15)
    return render_template('Day56.html', my_int=v, CURRENT_YEAR=dt.datetime.now().year, MY_NAME='Niloy')

@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    #genderize
    gender = requests.get('https://api.genderize.io?name='+name).json()['gender']
    #agify
    age = requests.get('https://api.agify.io/?name='+name).json()['age']
    return render_template('Day56.html', name=name, age=age, gender=gender)

@app.route('/blog')
def get_blog():
    posts = requests.get('https://api.npoint.io/6ed5a6c737255c0801f6').json()
    return render_template('Day56_blog.html', posts=posts)
    
if __name__ == '__main__':
    print("comes here")
    app.run(debug=True)