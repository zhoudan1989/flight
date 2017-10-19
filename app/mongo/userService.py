from . import db
from app.vo.user import user


class UserService:
    def insert(o):
        db.user.save(o.__dict__)

    def find(name):
        ret = []
        for i in db.user.find({"name": name}):
            ret.append(user(**i))
        return ret