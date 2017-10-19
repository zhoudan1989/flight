from . import app
from app.mongo.userService import UserService
from flask import render_template

@app.route('/user/page/<name>')
def userpage(name):
    users = UserService.find(name)
    return render_template("userPage.html",
                           users=users)
