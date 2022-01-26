import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from market.config import settings

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'
] = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'
app.config['SECRET_KEY'] = '278eb7681edbcd614fc60a3e'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from market import routes
