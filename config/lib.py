from typing import Optional
from fastapi import BackgroundTasks,FastAPI, Form, UploadFile, File, Body, Request, status, Response, Header
import uvicorn
import jwt
import time
import random
# Maria
import mariadb
import sys
#######
# Mongodb
import pymongo
from bson.objectid import ObjectId
#######

app = FastAPI()

# import requests