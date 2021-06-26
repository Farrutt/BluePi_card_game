from config.lib import *
from config.value import *
from method.game_process import *

# NEW GAME
@app.post("/new_game")
async def new_game(response: Response,request: Request):
    try:
        try:
            token_header = str(request.headers['authorization'])
            token_header = (token_header).split(' ')[1]
        except Exception as ex:
            response.status_code = 401
            return {"status_code" : 401,"message": 'Unauthorized',"data" : None}
        result_process = process_newgame(token_header)
        if result_process[0] == True:
            response.status_code = 200
            return {
                "status_code" : 200,
                "message": 'success',
                "data" : result_process[1]
                }
        else:
            response.status_code = 400
            return {
                "status_code" : 400,
                "message": 'fail',
                "data" : result_process[1]
                }
    except Exception as e:
        response.status_code = 400
        return {
            "status_code" : 400,
            "message": str(e),
            "data" : None
            }

# Get Global Score
@app.get("/get_global_score")
async def global_score(response: Response,request: Request):
    try:
        try:
            token_header = str(request.headers['authorization'])
            token_header = (token_header).split(' ')[1]
        except Exception as ex:
            response.status_code = 401
            return {"status_code" : 401,"message": 'Unauthorized',"data" : None}
        result_process = process_global_score(token_header)
        if result_process[0] == True:
            response.status_code = 200
            return {
                "status_code" : 200,
                "message": 'success',
                "data" : result_process[1]
                }
        else:
            response.status_code = 400
            return {
                "status_code" : 400,
                "message": 'fail',
                "data" : result_process[1]
                }
    except Exception as e:
        response.status_code = 400
        return {
            "status_code" : 400,
            "message": str(e),
            "data" : None
            }

# Get my score
@app.get("/get_my_score")
async def my_score(response: Response,request: Request):
    try:
        try:
            token_header = str(request.headers['authorization'])
            token_header = (token_header).split(' ')[1]
        except Exception as ex:
            response.status_code = 401
            return {"status_code" : 401,"message": 'Unauthorized',"data" : None}
        result_process = process_my_score(token_header)
        if result_process[0] == True:
            response.status_code = 200
            return {
                "status_code" : 200,
                "message": 'success',
                "data" : result_process[1]
                }
        else:
            response.status_code = 400
            return {
                "status_code" : 400,
                "message": 'fail',
                "data" : result_process[1]
                }
    except Exception as e:
        response.status_code = 400
        return {
            "status_code" : 400,
            "message": str(e),
            "data" : None
            }

@app.post("/action_open_card")
async def action_open_card(response: Response,request: Request):
    try:
        try:
            token_header = str(request.headers['authorization'])
            token_header = (token_header).split(' ')[1]
        except Exception as ex:
            response.status_code = 401
            return {"status_code" : 401,"message": 'Unauthorized',"data" : None}
        body_req = await request.json()
        transaction_id = body_req['transaction_id']
        position_row = int(body_req['position_row'])
        position_column = int(body_req['position_column'])
        result_process = process_open_card(token_header,transaction_id,position_column,position_row)
        if result_process[0] == True:
            response.status_code = 200
            return {
                "status_code" : 200,
                "message": 'success',
                "data" : result_process[1]
                }
        else:
            response.status_code = 400
            return {
                "status_code" : 400,
                "message": 'fail',
                "data" : result_process[1]
                }
    except Exception as e:
        response.status_code = 400
        return {
            "status_code" : 400,
            "message": str(e),
            "data" : None
            }

            