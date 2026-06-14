import getpass

LOG = True

USER = input("Username: ")
PASSWORD = getpass.getpass()

CONN_HOST = 'localhost'
CONN_PORT = 5672

API_URL = f'http://{CONN_HOST}:8000/api/'
