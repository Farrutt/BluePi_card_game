from config.lib import *
from config.db_connect import *
from config.mongo_connect import *
from function.generate_key import *
# app = FastAPI(debug=True)

# Test รับค่า body json
# @app.post("/test_body")
# async def test_body(request: Request):
#     aa = await request.json()
#     print ('YYY',aa)
#     return {"message": "Hello World"}


# Test รับค่า pararm
@app.get("/test_pararm")
async def find_mail_from_info(
    key: Optional[str] = None,
    ):
    list_card = [
        [ 
            {
                "number" : 6,
                "status_open" : True,
                "status_success" : True
            }, 
            {
                "number" : 5,
                "status_open" : True,
                "status_success" : True
            }, 
            {
                "number" : 5,
                "status_open" : True,
                "status_success" : True
            }, 
            {
                "number" : 2,
                "status_open" : True,
                "status_success" : True
            }
        ],
        [ 
            {
                "number" : 1,
                "status_open" : False,
                "status_success" : False
            }, 
            {
                "number" : 4,
                "status_open" : False,
                "status_success" : False
            }, 
            {
                "number" : 6,
                "status_open" : True,
                "status_success" : True
            }, 
            {
                "number" : 2,
                "status_open" : True,
                "status_success" : True
            }
        ],
        [ 
            {
                "number" : 4,
                "status_open" : False,
                "status_success" : False
            }, 
            {
                "number" : 1,
                "status_open" : False,
                "status_success" : False
            }, 
            {
                "number" : 3,
                "status_open" : False,
                "status_success" : False
            }, 
            {
                "number" : 3,
                "status_open" : False,
                "status_success" : False
            }
        ]
    ]
    c= {"status_open" : True}
    xx = [(i, colour.index(c))for i, card in enumerate(list_card)if c in card]
    print (xx)
    return {"message": "Hello World"}