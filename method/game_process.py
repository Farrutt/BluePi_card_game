from config.lib import *
from config.value import *
from database.db_select import *
from database.db_insert import *
from function.generate_card import *
from database.mongo_insert import *
from database.mongo_select import *
from function.action_click import *

def process_newgame(token_header):
    try:
        resul_select_token = select().select_id_by_token(token_header)
        if resul_select_token[0] == True and len(resul_select_token[1]) != 0:
            time_exp = resul_select_token[1][0]['time_exp']
            username = resul_select_token[1][0]['username']
            ts_now = int(time.time())
            if time_exp < ts_now:
                return [False,'Token has expire']
            result_random = random_card()
            if result_random[0] == True:
                result_insert = insert_mongo().insert_card(result_random[1],username,result_random[2])
                if result_insert[0] == True:
                    return [True,result_insert[1]]
                else:
                    return [False,result_insert[1]]
            else:
                return [False,result_random[1]]
        else:
            return [False,'Invalid Token']
    except Exception as e:
        return [False,str(e)]

def process_global_score(token_header):
    try:
        resul_select_token = select().select_id_by_token(token_header)
        if resul_select_token[0] == True and len(resul_select_token[1]) != 0:
            time_exp = resul_select_token[1][0]['time_exp']
            username = resul_select_token[1][0]['username']
            ts_now = int(time.time())
            if time_exp < ts_now:
                return [False,'Token has expire']
            result_select = select().select_global_score()
            if result_select[0] == True:
                return [True,result_select[1]]
            else:
                return [False,result_select[1]]
        else:
            return [False,'Invalid Token']
    except Exception as e:
        return [False,str(e)]

def process_my_score(token_header):
    try:
        resul_select_token = select().select_id_by_token(token_header)
        if resul_select_token[0] == True and len(resul_select_token[1]) != 0:
            time_exp = resul_select_token[1][0]['time_exp']
            username = resul_select_token[1][0]['username']
            ts_now = int(time.time())
            if time_exp < ts_now:
                return [False,'Token has expire']
            result_select = select().select_my_score(username)
            if result_select[0] == True:
                return [True,result_select[1]]
            else:
                return [False,result_select[1]]
        else:
            return [False,'Invalid Token']
    except Exception as e:
        return [False,str(e)]

def process_open_card(token_header,transaction_id,position_column,position_row):
    try:
        resul_select_token = select().select_id_by_token(token_header)
        if resul_select_token[0] == True and len(resul_select_token[1]) != 0:
            time_exp = resul_select_token[1][0]['time_exp']
            username = resul_select_token[1][0]['username']
            ts_now = int(time.time())
            if time_exp < ts_now:
                return [False,'Token has expire']
            result_select_game = select_mongo().select_transaction_card(transaction_id)
            if result_select_game[0] == True:
                if result_select_game[1]['status_game_success'] == False:
                    if result_select_game[1]['username'] == username:
                        card_all = result_select_game[1]['card']
                        click_count = result_select_game[1]['click']
                        number_of_cards = result_select_game[1]['number_of_cards']
                        result_action = func_action_one_click(transaction_id,card_all,position_column,position_row,click_count)
                        if result_action[0] == True:
                            result_click = result_action[2]
                            result_gen_response = gen_response_after_click(result_action[1])
                            if result_gen_response[0] == True:
                                result_check_success = func_check_game_success(transaction_id,result_action[1],number_of_cards,username,result_click)
                                result_score_now = func_get_score(username)
                                if result_score_now[0] == True:
                                    dict_data = {
                                        "card" : result_gen_response[1],
                                        "click" : result_click,
                                        "status_game" : result_check_success[1],
                                        "global_score" : result_score_now[1]['global'],
                                        "my_best" : result_score_now[1]['My']
                                    }
                                    return [True,dict_data]
                                else:
                                    return [False,result_score_now[1]]
                            else:
                                return [False,result_gen_response[1]]
                        else:
                            return [False,result_action[1]]
                    else:
                        return [False,'Invalid username in this transaction id']
                else:
                    return [False,'This game has been completed']
            else:
                return [False,result_select_game[1]]
        else:
            return [False,'Invalid Token']
    except Exception as e:
        print (e)
        return [False,str(e)]

