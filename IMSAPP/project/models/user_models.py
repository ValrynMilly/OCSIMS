from enum import unique
from flask_login import UserMixin
from project import db

#from project import users_db, Hatfield_db, Dordon_db, Andover_db, Erith_db, Purfleet_db, Avonmouth_db, Bicester_db, create_app, models
#users_db.create_all(app=create_app())

class User(UserMixin, db.Model):
    __bind_key__ = 'Users_db'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    role = db.Column(db.String(300))
    name = db.Column(db.String(100))