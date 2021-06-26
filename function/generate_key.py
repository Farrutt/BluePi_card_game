from config.lib import *
from config.value import *

def func_encode_token(payload):
    try:
        ts = str(time.time())
        encoded_jwt = jwt.encode(payload, ts, algorithm="HS256")
        encodes_data = encoded_jwt.decode('utf8').split('.')
        result_encode = encodes_data[0] +'.'+ encodes_data[1] +'.'+ encodes_data[2]
        return [True,result_encode]
    except Exception as e:
            return [False,str(e)]

def func_decode_token(data_encode):
    try:
        decode_jwt = jwt.decode(data_encode, secret_key, algorithms=["HS256"])
        return [True,decode_jwt]
    except Exception as e:
            return [False,str(e)]

def func_encode_login(payload):
    try:
        encoded_jwt = jwt.encode(payload, payload['password'], algorithm="HS256")
        encodes_data = encoded_jwt.decode('utf8').split('.')
        result_encode = encodes_data[0] +'.'+ encodes_data[1] +'.'+ encodes_data[2]
        return [True,result_encode]
    except Exception as e:
            return [False,str(e)]

def func_decode_login(data_encode,key):
    try:
        decode_jwt = jwt.decode(data_encode, key, algorithms=["HS256"])
        return [True,decode_jwt]
    except Exception as e:
            return [False,str(e)]
    