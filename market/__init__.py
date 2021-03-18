from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='5b9ab504c0f27d005f049658'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
from market import routes