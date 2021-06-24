from config.lib import *
from api.api import *

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8400, log_level="info",reload=True,workers=4)