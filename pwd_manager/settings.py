import os

SECRET_KEY = os.urandom(16)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f'sqlite:///pwd_manager.sqlite3'
