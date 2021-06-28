from config.lib import *
from config.value import *


# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user = MARIADB_USER,
        password = MARIADB_PASSWORD,
        host = MARIADB_HOST,
        port = MARIADB_PORT,
        database = MARIADB_DATABASE
    )
    # print ('conn:',conn)
    
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()