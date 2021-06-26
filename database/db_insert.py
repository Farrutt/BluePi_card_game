from config.lib import *
from config.value import *
from config.db_connect import *

class insert:
    def insert_user(self,username,data_encode):
        try:
            self.username = username
            self.data_encode = data_encode
            list_result = []
            text_sql = "INSERT INTO tb_account (username,data_encode,best_score) VALUES (%s, %s, %s)"
            data = (self.username,self.data_encode,None)
            cur.execute(text_sql, data)
            conn.commit()
            if cur.rowcount != 0:
                return [True,'insert success']
            else:
                return [False,'insert fails']
        except Exception as e:
            return [False,str(e)]

    def insert_token_user(self,username,data_encode,time_expire):
        try:
            self.username = username
            self.data_encode = data_encode
            self.time_expire = time_expire
            print (self.username)
            print (self.data_encode)
            list_result = []
            text_sql = "INSERT INTO tb_token (username,token,time_expire) VALUES (%s, %s, %s)"
            data = (self.username,self.data_encode,self.time_expire)
            cur.execute(text_sql, data)
            conn.commit()
            if cur.rowcount != 0:
                return [True,'insert success']
            else:
                return [False,'insert fails']
        except Exception as e:
            return [False,str(e)]