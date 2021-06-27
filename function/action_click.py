from config.lib import *
from config.value import *
from database.mongo_insert import *
from database.mongo_select import *
from database.mongo_update import *
from database.db_select import *
from database.db_insert import *
from database.db_update import *

def func_action_one_click(transaction_id,card_all,position_column,position_row,click_count):
    try:
        status_open_card = False
        status_find_match = False
        this_card = card_all[position_column][position_row]
        # print ('this_card:',this_card)
        this_card_number = this_card['number']
        this_status_open = this_card['status_open']
        this_status_success = this_card['status_success']
        if this_status_success == False:
            if this_status_open == False:
                for i in range(len(card_all)):
                    # print ('III_COLUMN_III:',i)
                    # print ('status_find_match_1:',status_find_match)
                    if status_find_match == False:
                        for y in range(len(card_all[i])):
                            # print ('YY_ROW_YY:',y)
                            # print ('status_find_match_2:',status_find_match)
                            if status_find_match == False:
                                if (card_all[i][y]['status_open'] == True and card_all[i][y]['status_success'] == False): #เจอไพ่ใบที่เปิดไว้และใบนั้นยังไม่เจอคู่
                                    # print ('IF 111')
                                    round_card_num = card_all[i][y]['number']
                                    if round_card_num == this_card_number: #ถ้าเจอคู่ที่ถูก
                                        # print ('IF 222')
                                        status_open_card = True #สถานะว่าเจอคู่
                                        card_all[i][y]['status_success'] = True #เปลี่ยนสถานะไพ่ใบที่เจอว่าเจอคู่แล้ว
                                        card_all[position_column][position_row]['status_open'] = True #เปลี่ยนสถานะไพ่ใบที่คลิกเลือกมาว่าถูกเปิดแล้ว
                                        card_all[position_column][position_row]['status_success'] = True #เปลี่ยนสถานะไพ่ใบที่คลิกเลือกมาว่าเจอคู่แล้ว
                                        status_find_match = True
                                        break
                                    else: #ถ้าคู่ไม่ถูก
                                        # print ('ELSE 111')
                                        status_open_card = False
                                        card_all[i][y]['status_open'] = False #คว่าไพ่ใบที่เจอ
                                        status_find_match = True
                                        break
                                elif (card_all[i][y]['status_open'] == False and card_all[i][y]['status_success'] == False): #ถ้าไพ่ใบที่เจอยังไม่เปิดและใบนั้นยังไม่เจอคู่
                                    # print ('ELIF 111')
                                    status_open_card = True
                                elif (card_all[i][y]['status_open'] == True and card_all[i][y]['status_success'] == True): #เจอไพ่ใบที่เปิดไว้และใบนั้นยังเจอคู่แล้ว
                                    # print ('ELIF 222')
                                    status_open_card = True
                                else: #ถ้าในเคสอื่นให้ผ่านไป
                                    # print ('ELSE 222')
                                    pass
                            else:
                                break
                    else:
                        break
                if status_open_card == True:
                    # print ('IF___status_open_card')
                    card_all[position_column][position_row]['status_open'] = True
                result_update_card = update_mongo().update_transaction_card_match(transaction_id,card_all,click_count)
                return [True,card_all,click_count+1]
            else:
                return [False,'This card has been open',None]
        else:
            return [False,'This card has been paired successfully',None]
    except IndexError:
        return [False,'Invalid position',None]
    except Exception as e:
        return [False,str(e),None]
    

def gen_response_after_click(card_all):
    try:
        for i in range(len(card_all)):
            for y in range(len(card_all[i])):
                if (card_all[i][y]['status_open'] == False and card_all[i][y]['status_success'] == False):
                    card_all[i][y]['number'] = None
        return [True,card_all]
    except Exception as e:
        return [False,str(e)]

def func_check_game_success(transaction_id,card_all,number_of_cards,username,result_click):
    try:
        count_success = 0
        for i in range(len(card_all)):
            for y in range(len(card_all[i])):
                if (card_all[i][y]['status_open'] == True and card_all[i][y]['status_success'] == True):
                    count_success += 1
                    if count_success == number_of_cards:
                        print ('game_success')
                        result_update_game = update_mongo().update_transaction_card_match_success(transaction_id)
                        if result_update_game[0] == True:
                            result_select_score = select().select_my_score(username)
                            print ('result_select_score:',result_select_score[1])
                            if result_select_score[0] == True:
                                if result_select_score[1] == None:
                                    result_update_score = update().update_my_score(username,result_click)
                                elif int(result_click) < int(result_select_score[1]):
                                    result_update_score = update().update_my_score(username,result_click)
                                    if result_update_score[0] == True:
                                        return [True,'Complete']
                                    else:
                                        return [False,result_update_score[1]]
                                else:
                                    return [True,'Complete']
                            else:
                                return [False,result_select[1]]
                            
                        else:
                            return [False,result_update_game[1]]
                    else:
                        pass
        return [True,'In_progress']
    except Exception as e:
        return [False,str(e)]

def func_get_score(username):
    try:
        result_select_global = select().select_global_score()
        result_select_me = select().select_my_score(username)
        if (result_select_global[0] == True and result_select_me[0] == True):
            dict_data = {
                "global" : result_select_global[1],
                "My" : result_select_me[1]
            }
            return [True,dict_data]
        else:
            return [False,'select_score_fail']
    except Exception as e:
        return [False,str(e)]