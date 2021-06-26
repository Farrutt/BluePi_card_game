from config.lib import *
from config.value import *
from database.db_select import *
from database.db_insert import *
from function.generate_key import *

def process_login(data_login):
    try:
        username = data_login['username']
        password = data_login['password']
        result_select = select().select_data_login(username)
        if result_select[0] == True and len(result_select[1]) != 0:
            data_encode = result_select[1][0]['data_encode']
            decode_data = func_decode_login(data_encode,password)
            if decode_data[0] == True:
                if username == decode_data[1]['username'] and password == decode_data[1]['password']:
                    token_user = func_encode_token(data_login)
                    ts_next = int(time.time())+86400
                    result_insert = insert().insert_token_user(username,token_user[1],ts_next)
                    print ('result_insert:',result_insert)
                    if result_insert[0] == True:
                        return [True,token_user[1]]
                    else:
                        return [False,'insert fails']
                else:
                    return [False,'Unauthorized '+ 'invalid username or password']
                
            else:
                return [False,'Unauthorized ' + 'invalid username or password']
            
        else:
            return [False,'Unauthorized ' + 'Not found user']

        
    except Exception as e:
            return [False,str(e)]

def process_add_user(data_user):
    try:
        username = data_user['username']
        password = data_user['password']
        encode_data = func_encode_login(data_user)
        if encode_data[0] == True:
            result_select = select().select_data_login(username)
            print ('result_select:',result_select)
            if result_select[0] == True and len(result_select[1]) == 0:
                result_insert = insert().insert_user(username,encode_data[1])
                if result_insert[0] == True:
                    return [True,data_user]
                else:
                    return [False,'insert fails']
            else:
                return [False,'username is exist']
        else:
            return [False,encode_data[1]]
        
    except Exception as e:
            return [False,str(e)]