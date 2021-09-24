import os


PROJECT_NAME = os.getenv('PROJECT_NAME', 'Help Children Backend')
MONGO_URL = os.getenv('MONGO_URL', 'mongodb://127.0.0.1:27017/')
API_V1_PREFIX = '/api/v1'

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

database_name = 'helpchildren'
users_collection_name = 'users'
roles_collection_name = 'roles'
