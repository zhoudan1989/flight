from app.route import app
from app.config.cfg import cfg

if __name__ == '__main__':
    app.run(port=cfg.getint("flask","port"))
