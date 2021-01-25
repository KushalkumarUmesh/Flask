from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)

app.config['SECRET_KEY']='f6108720d54a31c8280c3ead71f1c724'
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@localhost:3306/pypract" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

app.config['MAIRL_SERVER']='smtp.googlemail.com'
app.config['MAIRL_PORT']= 587
app.config['MAIRL_USE_TLS']= True
# app.config['MAIRL_USE_SSL']= True
app.config['MAIL_USERNAME']= 'kushalkumaru@gmail.com' #os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']= 'KushKush44' #os.environ.get('EMAIL_PASSWORD')

app.config['DEBUG']= True
mail = Mail(app)



from flaskblog import routes
