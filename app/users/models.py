from app.databese import BaseModel
from app.extensions import db
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref


class RolesUsers(BaseModel):
    __tablename__ = 'roles_users'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class Role(BaseModel, RoleMixin):
    __tablename__ = 'role'
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False) # crucial for flask-sequrity 
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))
    posts = relationship('Post', backref='auther', lazy=True)
    
    def __repr__(self):
	    return f'{self.__class__.__name__}({self.id}, {self.username})'