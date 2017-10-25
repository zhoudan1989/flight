from . import app
from flask import request,send_from_directory,abort


@app.route('/plot')
def plot():
    if request.method=="GET":
        return send_from_directory(app.root_path,"1.png",as_attachment=False)