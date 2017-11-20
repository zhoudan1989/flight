from flask import render_template
from . import app, socketio

@app.route('/wspage', methods=['GET', 'POST'])
def ws():
    return render_template('ws.html')

@socketio.on('message', namespace='/ws')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('json', namespace='/ws')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my event', namespace='/ws')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('connect', namespace='/ws')
def test_connect():
    print('Client connect')
    socketio.emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/ws')
def test_disconnect():
    print('Client disconnected')
