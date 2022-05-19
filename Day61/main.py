from flask import Flask, flash, render_template
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import StringField, PasswordField, SubmitField, EmailField
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.secret_key="super secret key"
class MyForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data=='12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)