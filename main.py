# -*- coding: utf-8 -*-
from config.lib import *
from config.value import *
from api.api import *
from api.login import *
from api.game import *

if __name__ == "__main__":
    if type_product == 'uat':
        uvicorn.run("main:app", host="0.0.0.0", port=8400, log_level="info",reload=True,workers=4)
    elif type_product == 'prod':
        uvicorn.run("main:app", host="0.0.0.0", port=8401, log_level="info",reload=True,workers=4)
    