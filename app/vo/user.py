class user:
    name = ""
    passwd = ""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)