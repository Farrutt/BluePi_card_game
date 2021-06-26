from config.lib import *
from config.value import *
from config.db_connect import *

class update:
    def update_my_score(self,username,score):
        try:
            print ('IN UPDATE')
            self.username = username
            self.score = score
            list_result = []
            text_sql = "UPDATE tb_account SET best_score = %d WHERE username = %s"
            data = (self.score,self.username)
            cur.execute(text_sql, data)
            conn.commit()
            if cur.rowcount != 0:
                return [True,'insert success']
            else:
                return [False,'insert fails']
        except Exception as e:
            print (e)
            return [False,str(e)]