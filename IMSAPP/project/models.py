from enum import unique
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Laptops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50), unique=True)
    model = db.Column(db.String(50))
    cpu = db.Column(db.String(50))
    ram = db.Column(db.String(50))
    storage = db.Column(db.String(50))
    operating_system = db.Column(db.String(50))
    assigned = db.Column(db.String(100))
