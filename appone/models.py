from appone.__init__ import db

class Student(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(40), unique=True, nullable=False)
    email=db.Column(db.String(30), unique=True, nullable=False)
    age=db.Column(db.Integer, nullable=False)
    password=db.Column(db.String(30), nullable=False)