from appone.__init__ import db
from flask import jsonify
from appone.models import Student


def con_create(data):
    user = Student.query.filter_by(name=data["name"]).first()
    if user:
        return jsonify(message="user already exist")
    db_user = Student(name=data["name"], email=data["email"],age=data["age"], password=data["password"])
    db.session.add(db_user)
    db.session.commit()
    return jsonify(message="user added successfully")

def con_fetch(id):
    user=Student.query.get(id)
    if user:
        return {"id":user.id, "name":user.name, "email":user.email, "password":user.pssword}
    return "enter the valid credentials"


def con_update(id, data):
    user=Student.query.get(id)
    if user:
        user.name=data["name"]
        user.email=data["email"]
        user.password=data["password"]
        db.session.commit()
        return "User added successfully"
    return "provide valid id"

def con_delete(id):
    user=Student.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return "user deleted successfully"
    return " provide the valid username"