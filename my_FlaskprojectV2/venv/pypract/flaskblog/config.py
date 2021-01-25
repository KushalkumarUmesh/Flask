import os

class Config:
    SECRET_KEY = 'f6108720d54a31c8280c3ead71f1c724' #os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/pypract"  #os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
        
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 #os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = True #os.environ.get('MAIL_USE_TLS')
    # app.config['MAIRL_USE_SSL']= True
    MAIL_USERNAME = 'kushalkumaru@gmail.com' #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = '8050703870' #os.environ.get('EMAIL_PASSWORD')
    # app.config['DEBUG']= True