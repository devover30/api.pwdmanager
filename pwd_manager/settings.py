import os
from pathlib import Path
SECRET_KEY = os.urandom(16)

SQLALCHEMY_TRACK_MODIFICATIONS = False
dbFileDir = Path.cwd().joinpath('models')
if not dbFileDir.exists():
    os.makedirs(str(dbFileDir))
dbFileName = 'pwd_manager.sqlite3'
dbURI = f'{str(dbFileDir)}/{dbFileName}'
SQLALCHEMY_DATABASE_URI = f'sqlite:///{dbURI}'
