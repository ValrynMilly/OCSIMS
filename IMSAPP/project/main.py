from urllib import request
from importlib import reload
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import insert
from . import db
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .models.site_models import Laptops

main = Blueprint('main', __name__)
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    laptop_count = Laptops.query.count()
    laptop_assigned = Laptops.query.filter(Laptops.assigned == 'Yes').count()
    laptop_unassigned = Laptops.query.filter(Laptops.assigned == 'No').count()
    db.session.commit()
    return render_template('dashboard.html',name=current_user.name, 
    laptop_count=laptop_count, 
    laptop_assigned=laptop_assigned, 
    laptop_unassigned=laptop_unassigned)

@main.route('/laptops', methods=['POST', 'GET'])
@login_required
def laptops():
    if request.method == "POST":
        new_laptop_form_name = request.form['Name']
        new_laptop_form_manufacturer = request.form['Manufacturer']
        new_laptop_form_model = request.form['Model']
        new_laptop_form_cpu = request.form['CPU']
        new_laptop_form_ram = request.form['RAM']
        new_laptop_form_storage = request.form['Storage']
        new_laptop_form_OS = request.form['Operating_System']
        new_laptop_form_ma = request.form['Mac_address']
        new_laptop_form_location = request.form.get('Location')
        new_laptop_form_assigned = request.form.get('assigned')
        new_laptop_form_assigned_to = request.form['Assigned_to']
        try:
            new_laptop = Laptops(name=new_laptop_form_name, manufactor=new_laptop_form_manufacturer, 
            model=new_laptop_form_model, cpu=new_laptop_form_cpu, ram=new_laptop_form_ram, storage=new_laptop_form_storage, 
            operating_system=new_laptop_form_OS, mac_address = new_laptop_form_ma, location=new_laptop_form_location,
            assigned=new_laptop_form_assigned, assigned_to=new_laptop_form_assigned_to)
            db.session.add(new_laptop)
            db.session.commit()
            return redirect('/laptops')
        except:
            "There was an error adding your data"
    else:
        laptop = Laptops.query
        return render_template('laptops.html', laptop=laptop)

@main.route('/update/<int:id>', methods=['POST', 'GET'])
@login_required
def update(id):
    laptop_update = Laptops.query.get_or_404(id)
    if request.method == "POST":
        laptop_update.model = request.form['Name']
        laptop_update.manufactor = request.form['Manufacturer']
        laptop_update.model = request.form['Model']
        laptop_update.cpu = request.form['CPU']
        laptop_update.ram = request.form['RAM']
        laptop_update.storage = request.form['Storage']
        laptop_update.operating_system = request.form['Operating_System']
        laptop_update.mac_address = request.form['Mac_address']
        laptop_update.assigned = request.form.get('Location')
        laptop_update.assigned = request.form.get('assigned')
        laptop_update.assigned_to = request.form['Assigned_to']
        try:
            db.session.commit()
            return redirect('/laptops')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update.html', laptop_update=laptop_update)

@main.route('/delete/<int:id>')
@login_required
def delete(id):
    laptop_delete = Laptops.query.get_or_404(id)

    try:
        db.session.delete(laptop_delete)
        db.session.commit()
        return redirect('/laptops')
    except:
        return "There was an issue deleting that laptop im sorry :("