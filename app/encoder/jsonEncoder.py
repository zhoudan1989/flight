import json
from bson import ObjectId

class jsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, object):
            return o.__dict__
        return json.JSONEncoder.default(self, o)