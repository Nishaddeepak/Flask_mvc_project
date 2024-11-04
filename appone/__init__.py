from flask import Flask
from config import Config
# from appone.models import Student
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config.from_object(Config)

db =SQLAlchemy(app)

from appone.views import *

