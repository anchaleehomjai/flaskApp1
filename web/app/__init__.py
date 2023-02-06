from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '563eec0f9a31cd7c6a59d840a32336116d58f2cffd8de84a'
app.config['JSON_AS_ASCII'] = False
 
from app import views  # noqa

 