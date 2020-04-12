from os import environ

SECRET_KEY = environ.get('SECRET_KEY', '3d6f45a5fc12445dbac2f59c3b6c7cb1')
DB_USERNAME = environ.get('DB_USERNAME', 'develop')
DB_PASSWORD = environ.get('DB_PASSWORD', 'Aa123456!')
DB_NAME = environ.get('DB_NAME', 'my_db')
DB_PORT = int(environ.get('DB_PORT', '3306'))
DB_HOST = environ.get('DB_HOST', 'localhost')
APP_HOST = environ.get('APP_HOST', 'localhost')
APP_PORT = int(environ.get('APP_PORT', '5050'))
APP_NAME = environ.get('APP_NAME', 'TodoFlask')
REDIS_ADDRESS = environ.get('REDIS_ADDRESS', 'localhost:6379')
