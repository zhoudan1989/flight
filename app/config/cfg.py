import configparser


class fligtConfig:
    def __init__(self):
        cfg = configparser.ConfigParser()
        cfg.read("cfg.ini")


cfg = fligtConfig()