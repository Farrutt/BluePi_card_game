from config.lib import *
type_product = 'prod'
print('type_product:',type_product)

if type_product == 'prod':
    secret_key = 'secret_key'
    # MariaDB
    MARIADB_USER = 'root'
    MARIADB_PASSWORD = ""
    MARIADB_HOST = "localhost"
    MARIADB_PORT = 3306
    MARIADB_DATABASE ="BluePi"
    #MongoDB
    URL_MONGO = "mongodb://localhost:27017/"
    DB_MONGO = "Card_game"

elif type_product == 'uat':
    secret_key = 'secret_key'
    # MariaDB
    MARIADB_USER = 'root'
    MARIADB_PASSWORD = ""
    MARIADB_HOST = "localhost"
    MARIADB_PORT = 3306
    MARIADB_DATABASE ="BluePi"
    #MongoDB
    URL_MONGO = "mongodb://localhost:27017/"
    DB_MONGO = "Card_game"
