import os
from flask import Flask
from werkzeug.debug import DebuggedApplication
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_folder='static')

# this DEBUG config here will be overridden by FLASK_DEBUG shell environment
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ae7b9205c7a88aafaeb8f4a66493c3531e63df8ef9a9a770'
app.config['JSON_AS_ASCII'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'lab13_login'
login_manager.init_app(app)

from app import views  # noqa
