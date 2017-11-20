from app.config.cfg import cfg
from app.route import app, socketio

if __name__ == '__main__':
    socketio.run(app, port=cfg.getint("flask", "port"))
