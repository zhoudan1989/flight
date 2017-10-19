from flask import Flask

app = Flask(__name__)

from .userRoutes import *
from .home import *
from .plotRoutes import *
from .userPageRoutes import *
