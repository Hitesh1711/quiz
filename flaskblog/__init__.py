from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY']='364172c4502c6c035b0d3070b54e4002'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view =  'login'  # the login is the name of the function of the login function that we createed in routes.py
login_manager.login_message_category= 'info'

from flaskblog import routes