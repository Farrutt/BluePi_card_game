from config.lib import *
from config.value import *
from config.mongo_connect import *

class insert_mongo:
    def insert_card(self,data_card,username,number_of_card):
        try:
            self.data_card = data_card
            self.username = username
            mycol = mydb["transaction_card"]
            dic_insert = {
                "username" : username,
                "number_of_cards" : number_of_card,
                "card" : data_card,
                "click" : 0,
                "status_game_success" : False,
                "CreateAt" : datetime.datetime.utcnow(),
                "UpdateAt" : datetime.datetime.utcnow()
            }
            result_insert = mycol.insert_one(dic_insert)
            id_game = str(result_insert.inserted_id)
            return [True,id_game]
        except Exception as e:
            return [False,str(e)]