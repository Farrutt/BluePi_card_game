from config.lib import *
from config.value import *
from config.db_connect import *

class select:
    def select_data_login(self,username):
        try:
            self.username = username
            list_result = []
            text_sql = "SELECT username,data_encode FROM tb_account WHERE username=%s"
            data = (self.username,)
            cur.execute(text_sql, data)
            for (username_db,data_encode) in cur:
                dict_data = {
                    'username_db' : username_db,
                    'data_encode' : data_encode
                }
                list_result.append(dict_data)
            return [True,list_result]
        except Exception as e:
            return [False,str(e)]

    def select_id_by_token(self,token):
        try:
            self.token = token
            list_result = []
            text_sql = "SELECT id,time_expire,username FROM tb_token WHERE token=%s"
            data = (self.token,)
            cur.execute(text_sql, data)
            for (id_data,time_expire,username) in cur:
                dict_data = {
                    'id' : id_data,
                    'time_exp' : time_expire,
                    'username' : username
                }
                list_result.append(dict_data)
            return [True,list_result]
        except Exception as e:
            return [False,str(e)]

    def select_global_score(self):
        try:
            list_result = []
            text_sql = "SELECT MIN(best_score) FROM tb_account"
            cur.execute(text_sql)
            myresult = cur.fetchone()
            return [True,myresult[0]]
        except Exception as e:
            return [False,str(e)]

    def select_my_score(self,username):
        try:
            list_result = []
            self.username = username
            text_sql = "SELECT best_score FROM tb_account WHERE username=%s"
            data = (self.username,)
            cur.execute(text_sql,data)
            for (score) in cur:
                my_score = list(score)
            return [True,my_score[0]]
        except Exception as e:
            return [False,str(e)]