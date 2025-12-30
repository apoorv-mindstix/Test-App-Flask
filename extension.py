from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
# from .dbeven import enable_sqlite_fk


db = SQLAlchemy()
jwt = JWTManager()
