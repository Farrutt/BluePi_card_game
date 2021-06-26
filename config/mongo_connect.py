from config.lib import *
from config.value import *

# Connect mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# My DB
mydb = myclient["Card_game"]