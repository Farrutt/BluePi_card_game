from config.lib import *
from config.value import *
from method.login_process import *
# app = FastAPI(debug=True)

@app.post("/login")
async def login(request: Request,response: Response):
    try:
        data_login = await request.json()
        result_process = process_login(data_login)
        if result_process[0] == True:
            response.status_code = 200
            return {
                "status_code" : 200,
                "message": 'login success',
                "data" : result_process[1]
                }
        else:
            response.status_code = 401
            return {
                "status_code" : 401,
                "message": result_process[1],
                "data" : None
                }
    except Exception as e:
        response.status_code = 401
        return {
            "status_code" : 401,
            "message": str(e),
            "data" : None
            }

@app.post("/add_user")
async def login(request: Request,response: Response):
    try:
        data_user = await request.json()
        result_process = process_add_user(data_user)
        if result_process[0] == True:
            response.status_code = 200
            return {
                "status_code" : 200,
                "message": 'add_user success',
                "data" : result_process[1]
                }
        else:
            response.status_code = 400
            return {
                "status_code" : 400,
                "message": result_process[1],
                "data" : None
                }
    except Exception as e:
        response.status_code = 400
        return {
            "status_code" : 400,
            "message": str(e),
            "data" : None
            }
