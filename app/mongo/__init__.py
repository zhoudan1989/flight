from pymongo import MongoClient
from app.config.cfg import cfg

client = MongoClient(cfg.get("mongo", "host"), cfg.getint("mongo", "port"))
db = client[cfg.get("mongo", "db_name")]
