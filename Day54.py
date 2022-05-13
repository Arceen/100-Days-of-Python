from flask import Flask
import os
from os import environ
import random
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '''
# <center>
# <h1>HOOOOOOOO</h1>
# <p>Hello, World!</p>
# <br/>
# <p>My name is Don</p>
# <iframe src="https://giphy.com/embed/lZZwR5gvWDYdFcGNf7" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/lZZwR5gvWDYdFcGNf7">via GIPHY</a></p>
# </center>
# '''



# def make_bold(f):
#     def wrapper():
#         return '<strong>'+f()+'</strong>'
#     return wrapper
    
# def make_italic(f):
#     def wrapper():
#         return '<em>'+f()+'</em>'
#     return wrapper

# def make_underlined(f):
#     def wrapper():
#         return '<u>'+f()+'</u>'
#     return wrapper

# @app.route("/bye")
# @make_underlined
# @make_italic
# @make_bold
# def bye():
#     return "Bye!"

# @app.route('/<whoami>')
# def description(whoami):
#     return f'Welcome to ur w'\
#         'ebiste {whoami}'
# @app.route('/language/<var>')
# def language(var):
#     return var


# if __name__ == '__main__':
#     app.run()

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False


# def check_logged_in(f):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             f(args[0])
#         else:
#             print("nothing for you")
#     return wrapper
# @check_logged_in
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")

# new_user = User("angela")
# new_user.is_logged_in = True
# create_blog_post(new_user)

# # Create the logging_decorator() function 👇
# def logging_decorator(f):
#   def wrapper(*args):
#     print(f"You called {f.__name__}({', '.join(list(map(str, args)))})")
#     print(f"It returned: {f(*args)}")
#   return wrapper   

# # Use the decorator 👇
# @logging_decorator
# def a_function(*args):
#   return sum(args)

# a_function(1,2,3)

app = Flask(__name__)
my_int = random.randint(0,9)
# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/')
def game_start():
    return '''
<h1>Guess a number between 0 and 9</h1>
<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />
'''

@app.route('/<number>')
def guess(number):
    number = int(number)
    color = 'green'
    header = 'You found me!'
    link = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
    if number < my_int:
        color = 'red'
        header = 'Too low, try again!'
        link = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
    elif number > my_int:
        color = 'purple'
        header = 'Too high, try again!'
        link = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
    
    return f'<h1 style="color:{color}">{header}</h1><img src="{link}"/>'