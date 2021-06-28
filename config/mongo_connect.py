from config.lib import *
from config.value import *

# Connect mongodb
myclient = pymongo.MongoClient(URL_MONGO)

# My DB
mydb = myclient[DB_MONGO]