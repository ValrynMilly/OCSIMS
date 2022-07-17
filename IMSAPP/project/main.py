from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import insert
from . import db
from .models import Laptops

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/laptops', methods=['POST', 'GET'])
@login_required
def laptops():
    if request.method == "POST":
        new_laptop_form_manufacturer = request.form['Manufacturer']
        new_laptop_form_model = request.form['Model']
        new_laptop_form_cpu = request.form['CPU']
        new_laptop_form_ram = request.form['RAM']
        new_laptop_form_storage = request.form['Storage']
        new_laptop_form_OS = request.form['Operating_System']
        new_laptop_form_assigned = request.form['Assigned']
        new_laptop_var_man = new_laptop_form_manufacturer
        new_laptop_var_mod = new_laptop_form_model
        new_laptop_var_cpu = new_laptop_form_cpu
        new_laptop_var_ram = new_laptop_form_ram
        new_laptop_var_storage = new_laptop_form_storage
        new_laptop_var_os = new_laptop_form_OS
        new_laptop_var_ass = new_laptop_form_assigned
        try:
            new_laptop = Laptops(manufactor=new_laptop_var_man, model=new_laptop_var_mod, cpu=new_laptop_var_cpu, ram=new_laptop_var_ram, storage=new_laptop_var_storage, operating_system=new_laptop_var_os, assigned=new_laptop_var_ass)
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
        laptop_update.manufactor = request.form['Manufacturer']
        laptop_update.model = request.form['Model']
        laptop_update.cpu = request.form['CPU']
        laptop_update.ram = request.form['RAM']
        laptop_update.storage = request.form['Storage']
        laptop_update.operating_system = request.form['Operating_System']
        laptop_update.assigned = request.form['Assigned']
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