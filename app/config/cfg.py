import configparser


class fligtConfig:
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read("cfg.ini")

    def get(self, section, option):
        return self.cfg.get(section, option)

    def getint(self, section, option):
        return self.cfg.getint(section, option)

cfg = fligtConfig()