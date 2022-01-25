from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from market.config import settings

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'
] = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

db = SQLAlchemy(app)

from market import routes
