from enum import unique
from flask_login import UserMixin
from project import db

#from project import db, create_app, models
#users_db.create_all(app=create_app())

class Laptops(db.Model):
    __bind_key__ = 'Site_db'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    cpu = db.Column(db.String(50))
    ram = db.Column(db.String(50))
    storage = db.Column(db.String(50))
    operating_system = db.Column(db.String(50))
    mac_address = db.Column(db.String(100))
    location = db.Column(db.String(50))
    assigned = db.Column(db.String(100))
    assigned_to = db.Column(db.String(30))
    notes = db.Column(db.String(5000))

class Desktops(db.Model):
    __bind_key__ = 'Site_db'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    cpu = db.Column(db.String(50))
    ram = db.Column(db.String(50))
    storage = db.Column(db.String(50))
    operating_system = db.Column(db.String(50))
    mac_address = db.Column(db.String(100))
    location = db.Column(db.String(50))

class Mobile_Phone(db.Model):
    __bind_key__ = 'Site_db'
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    display = db.Column(db.String(50))
    cpu = db.Column(db.String(50))
    storage = db.Column(db.String(50))
    operating_system = db.Column(db.String(50))
    location = db.Column(db.String(50))

class SimCards(db.Model):
    __bind_key__ = 'Site_db'
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50))
    amount = db.Column(db.Integer)
    location = db.Column(db.String(50))

class Monitors(db.Model):
    __bind_key__ = 'Site_db'
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    max_res = db.Column(db.String(50))
    panel_type = db.Column(db.String(50))
    refresh_rate = db.Column(db.String(50))
    inputs = db.Column(db.String(100))
    mac_address = db.Column(db.String(100))
    location = db.Column(db.String(100))

class Printers(db.Model):
    __bind_key__ = 'Site_db'
    id = db.Column(db.Integer, primary_key=True)
    manufactor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    mac_address = db.Column(db.String(100))
    location = db.Column(db.String(100))

class Tools(db.Model):
    __bind_key__ = 'Site_db'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    description = db.Column(db.String(100))
    amount = db.Column(db.Integer)

class Accessories(db.Model):
    __bind_key__ = 'Site_db'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    description = db.Column(db.String(100))
    amount = db.Column(db.Integer)