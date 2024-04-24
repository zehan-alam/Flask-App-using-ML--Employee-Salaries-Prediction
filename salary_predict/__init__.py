# Install packages - flask, flask-sqlite, flask-wtf, wtforms

from flask import Flask # type: ignore

app = Flask(__name__) # <-- Initiates App
app.config['SECRET_KEY'] = '778af7ea77cee5d509ac2904'

from salary_predict import routes # <-- adding the routes file to our app