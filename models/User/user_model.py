from app import db
from flask_login import UserMixin
from sqlalchemy import Enum
import enum

class UserRole(enum.Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    MEMBER = "member"

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(
        Enum(UserRole, name="user_role_enum"),
        nullable=False
    )

    def __repr__(self):
        return f'User with name {self.name} and role {self.role}'
    
    def get_id(self):
        return self.uid