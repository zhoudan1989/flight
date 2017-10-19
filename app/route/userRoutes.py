from . import app
from flask import request
from app.encoder.jsonEncoder import jsonEncoder
from app.mongo.userService import UserService
from app.vo.user import user


@app.route('/user/<name>',methods=['GET', 'POST'])
def finduser(name):
    if request.method == "GET":
        return jsonEncoder().encode(UserService.find(name))
    elif request.method == "POST":
        return "post"
    elif request.method == "DELETE":
        return "delete"


@app.route('/insertUser/<name>')
def insertuser(name):
    u = user()
    u.name = name
    u.passwd = request.values["passwd"]#request.args  request.from
    UserService.insert(u)#getattr(UserService,"insert")(u)
    return "ok"