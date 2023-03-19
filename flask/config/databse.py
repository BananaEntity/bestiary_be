import os

# Connection URL format: postgres://username:password@hostname/databasename 
POSTGRE_URL = 'postgresql://{}:{}@{}/{}'.format(
    os.getenv('POSTGRE_USER', default=None),
    os.getenv('POSTGRE_PASSWORD', default=None),
    os.getenv('POSTGRE_HOST', default=None),
    os.getenv('POSTGRE_DATEBASE', default=None)
)