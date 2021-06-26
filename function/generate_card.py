from config.lib import *
from config.value import *

def random_card():
    try:
        list_random = []
        list_random_all = []
        list_number = [1,2,3,4,5,6,1,2,3,4,5,6]
        number_of_card = len(list_number)
        random.shuffle(list_number)
        for i in list_number:
            data_dict = {
                "number" : i,
                "status_open" : False,
                "status_success" : False
            }
            list_random.append(data_dict)
            if len(list_random) == 4:
                list_random_all.append(list_random)
                list_random = []
        return [True,list_random_all,number_of_card]
    except Exception as e:
            return [False,str(e),None]
