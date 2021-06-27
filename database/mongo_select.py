from config.lib import *
from config.value import *
from config.mongo_connect import *

class select_mongo:
    def select_transaction_card(self,transaction_id):
        try:
            self.transaction_id = transaction_id
            mycol = mydb["transaction_card"]
            result_select_card = mycol.find_one({"_id" : ObjectId(transaction_id)})
            if result_select_card != None:
                result_select_card['_id'] = str(result_select_card['_id'])
                return [True,result_select_card]
            else:
                return [False,'Not found transaction_id']
        except Exception as e:
            return [False,str(e)]         