from flask import request, jsonify
from appone.__init__ import app
from appone import controllers

@app.route("/")
def home():
    return "This is home"

@app.route("/about", methods=["GET"])
def about_func():
    return jsonify( message="this is from about page")


@app.route("/create_user", methods=["POST"])
def user_add():
    data=request.get_json()
    res=controllers.con_create(data)
    return "Employee Created"

@app.route("/fetch_user/<id>", methods=["GET"])
def get_data(id):
    res=controllers.con_fetch(id)
    return res

@app.route("/update/<id>", methods=["PUT"])
def update_data(id):
    data=request.get_json()
    res=controllers.con_update(id, data)
    return res


@app.route("/delete/<id>", methods=["DELETE"])
def delete_data(id):
    # data=Student.query.get(id)
    res=controllers.con_delete(id)
    return res


