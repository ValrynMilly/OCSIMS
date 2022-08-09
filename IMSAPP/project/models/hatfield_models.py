from enum import unique
from flask_login import UserMixin
from project import db

#from project import users_db, Hatfield_db, Dordon_db, Andover_db, Erith_db, Purfleet_db, Avonmouth_db, Bicester_db, create_app, models
#users_db.create_all(app=create_app())

class Laptops(db.Model):
    __bind_key__ = 'Hatfield_db'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    cpu = db.Column(db.String(50))
    ram = db.Column(db.String(50))
    storage = db.Column(db.String(50))
    operating_system = db.Column(db.String(50))
    mac_address = db.Column(db.String(100))
    assigned = db.Column(db.String(100))
    assigned_to = db.Column(db.String(30))

class Desktops(db.Model):
    __bind_key__ = 'Hatfield_db'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    cpu = db.Column(db.String(50))
    ram = db.Column(db.String(50))
    storage = db.Column(db.String(50))
    operating_system = db.Column(db.String(50))
    mac_address = db.Column(db.String(100))
    assigned = db.Column(db.String(100))
    assigned_to = db.Column(db.String(30))

class Mobile_Phone(db.Model):
    __bind_key__ = 'Hatfield_db'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    display = db.Column(db.String(50))
    cpu = db.Column(db.String(50))
    storage = db.Column(db.String(50))
    operating_system = db.Column(db.String(50))
    mac_address = db.Column(db.String(100))
    assigned = db.Column(db.String(100))
    assigned_to = db.Column(db.String(30))

class Monitors(db.Model):
    __bind_key__ = 'Hatfield_db'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    max_res = db.Column(db.String(50))
    panel_type = db.Column(db.String(50))
    refresh_rate = db.Column(db.String(50))
    inputs = db.Column(db.String(100))
    mac_address = db.Column(db.String(100))
    assigned = db.Column(db.String(100))
    assigned_to = db.Column(db.String(30))

class Printers(db.Model):
    __bind_key__ = 'Hatfield_db'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    mac_address = db.Column(db.String(100))
    assigned = db.Column(db.String(100))
    assigned_to = db.Column(db.String(30))