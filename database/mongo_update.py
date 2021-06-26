from config.lib import *
from config.value import *
from config.mongo_connect import *

class update_mongo:
    def update_transaction_card_match(self,transaction_id,card_all,click_count):
        try:
            self.transaction_id = transaction_id
            self.card_all = card_all
            self.click_count = int(click_count) + 1 
            mycol = mydb["transaction_card"]
            text_find = { "_id": ObjectId(self.transaction_id) }
            text_update = { "$set": { "click": self.click_count,"card":self.card_all}}
            result_update_card = mycol.update_one(text_find,text_update)
            if result_update_card.modified_count != 0:
                return [True,'update success']
            else:
                return [False,'update_fails']
        except Exception as e:
            return [False,str(e)]

    def update_transaction_card_match_success(self,transaction_id):
        try:
            self.transaction_id = transaction_id
            mycol = mydb["transaction_card"]
            text_find = { "_id": ObjectId(self.transaction_id) }
            text_update = { "$set": { "status_game_success" : True}}
            result_update_card = mycol.update_one(text_find,text_update)
            if result_update_card.modified_count != 0:
                return [True,'update_success']
            else:
                return [False,'update_fails']
        except Exception as e:
            print ('update_except:',e)
            return [False,str(e)]