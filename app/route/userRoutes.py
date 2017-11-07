from flask import request

from app.encoder.jsonEncoder import jsonEncoder
from app.mongo.userService import UserService
from app.util.importutils import import_class
from app.vo.user import user
from . import app


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
    #UserService.insert(u)
    getattr(import_class("app.mongo.userService.UserService"),"insert")(u)
    return "ok"