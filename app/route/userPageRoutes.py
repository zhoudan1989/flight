from . import app
from app.mongo.userService import UserService
from flask import render_template
import pygal

@app.route('/user/page/<name>')
def userpage(name):
    users = UserService.find(name)
    return render_template("userPage.html",
                           users=users)

@app.route('/polt/page')
def poltpage():
    polt = pygal.Bar();
    polt.add('A',(1, 3, 3, 7))
    polt.add('B',(1, 6, 6, 4))
    return render_template("polt.html",
                           chart=polt)
