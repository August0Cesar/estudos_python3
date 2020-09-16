import os

SECRET_KEY = 'augusto'

# Configuração de banco
MYSQL_HOST = "172.17.0.2"
MYSQL_USER = "root"
MYSQL_PASSWORD = "test"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'