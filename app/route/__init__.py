from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from .userRoutes import *
from .home import *
from .plotRoutes import *
from .userPageRoutes import *
from .websocketRoutes import *
