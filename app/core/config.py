import os


PROJECT_NAME = os.getenv('PROJECT_NAME', 'Help Children Backend')
MONGO_URL = os.getenv('MONGO_URL', 'mongodb://127.0.0.1:27017/')
API_V1_PREFIX = '/api/v1'

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
JWT_SECRET = '0lwlpxEzgAfGucwZaIRTWOpqnybX2vOvrPbOTwvs'

database_name = 'helpchildren'
users_collection_name = 'users'
pupils_collection_name = 'pupils'
roles_collection_name = 'roles'
regions_collection_name = 'regions'
events_collection_name = 'events'


accounts_roles = {
    0: 'pupil',
    1: 'volunteer',
    2: 'sponsor',
    3: 'mentor',
    4: 'company',
    5: 'orphanage',  # детдом
    6: 'district_administration',
    7: 'federal_administration',
}

event_status = {
    0: 'finished',
    1: 'gathering',
    2: 'pending',
    3: 'cancelled_by_owner',
    4: 'cancelled_due_to_funds_shortage',
}
