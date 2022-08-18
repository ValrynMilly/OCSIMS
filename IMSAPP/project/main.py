from urllib import request
from importlib import reload
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import insert, and_
from sqlalchemy.sql import func, select
from . import db
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .models.site_models import *

main = Blueprint('main', __name__)

engine = db.create_engine


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    laptop_count = Laptops.query.count()
    laptop_assigned = Laptops.query.filter(Laptops.assigned == 'Yes').count()
    laptop_unassigned = Laptops.query.filter(Laptops.assigned == 'No').count()
    desktop_count = Desktops.query.count()
    mobile_phone_count = Mobile_Phone.query.count()
    sim_card_count = SimCards.query.with_entities(func.sum(SimCards.amount).label('total')).first().total
    return render_template('dashboard.html',name=current_user.name, 
    laptop_count=laptop_count, laptop_assigned=laptop_assigned, laptop_unassigned=laptop_unassigned, 
    desktop_count=desktop_count, 
    mobile_phone_count=mobile_phone_count, 
    sim_card_count=sim_card_count)

########################## INVENTORY ROUTES/FUNCTIONS ##########################

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

@main.route('/desktops', methods=['POST', 'GET'])
@login_required
def desktops():
    if request.method == "POST":
        new_desktop_form_name = request.form['Name']
        new_desktop_form_manufacturer = request.form['Manufacturer']
        new_desktop_form_model = request.form['Model']
        new_desktop_form_cpu = request.form['CPU']
        new_desktop_form_ram = request.form['RAM']
        new_desktop_form_storage = request.form['Storage']
        new_desktop_form_OS = request.form['Operating_System']
        new_desktop_form_ma = request.form['Mac_address']
        new_desktop_form_location = request.form.get('Location')
        try:
            new_desktop = Desktops(name=new_desktop_form_name, manufactor=new_desktop_form_manufacturer, 
            model=new_desktop_form_model, cpu=new_desktop_form_cpu, ram=new_desktop_form_ram, storage=new_desktop_form_storage, 
            operating_system=new_desktop_form_OS, mac_address = new_desktop_form_ma, location=new_desktop_form_location)
            db.session.add(new_desktop)
            db.session.commit()
            return redirect('/desktops')
        except:
            "There was an error adding your data"
    else:
        desktop = Desktops.query
        return render_template('desktops.html', desktop=desktop)

@main.route('/mobile_phones', methods=['POST', 'GET'])
@login_required
def mobile_phones():
    if request.method == "POST":
        new_mobile_phone_form_manufacturer = request.form['Manufacturer']
        new_mobile_phone_form_model = request.form['Model']
        new_mobile_phone_form_display = request.form['Display']
        new_mobile_phone_form_cpu = request.form['CPU']
        new_mobile_phone_form_storage = request.form['Storage']
        new_mobile_phone_form_OS = request.form['Operating_System']
        new_mobile_phone_form_location = request.form.get('Location')
        try:
            new_mobile_phone = Mobile_Phone(manufactor=new_mobile_phone_form_manufacturer, 
            model=new_mobile_phone_form_model, cpu=new_mobile_phone_form_cpu, display=new_mobile_phone_form_display, storage=new_mobile_phone_form_storage, 
            operating_system=new_mobile_phone_form_OS, location=new_mobile_phone_form_location)
            db.session.add(new_mobile_phone)
            db.session.commit()
            return redirect('/mobile_phones')
        except:
            "There was an error adding your data"
    else:
        mobile_phones = Mobile_Phone.query
        return render_template('mobile_phones.html', mobile_phones=mobile_phones)

@main.route('/sim_cards', methods=['POST', 'GET'])
@login_required
def sim_cards():
    if request.method == "POST":
        new_sim_card_form_provider = request.form['Provider']
        new_sim_card_form_amount = request.form['Amount']
        new_sim_card_form_location = request.form['Location']
        try:
            new_sim_card = SimCards(provider=new_sim_card_form_provider, 
            amount=new_sim_card_form_amount, location=new_sim_card_form_location)
            db.session.add(new_sim_card)
            db.session.commit()
            return redirect('/sim_cards')
        except:
            "There was an error adding your data"
    else:
        sim_cards = SimCards.query
        return render_template('sim_cards.html', sim_cards=sim_cards)



########################## UPDATE FUNCTIONS ##########################

@main.route('/update_laptop/<int:id>', methods=['POST', 'GET'])
@login_required
def update_laptop(id):
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
        laptop_update.location = request.form.get('Location')
        laptop_update.assigned = request.form.get('assigned')
        laptop_update.assigned_to = request.form['Assigned_to']
        try:
            db.session.commit()
            return redirect('/laptops')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update_laptop.html', laptop_update=laptop_update)

@main.route('/update_desktop/<int:id>', methods=['POST', 'GET'])
@login_required
def update_desktop(id):
    desktop_update = Desktops.query.get_or_404(id)
    if request.method == "POST":
        desktop_update.model = request.form['Name']
        desktop_update.manufactor = request.form['Manufacturer']
        desktop_update.model = request.form['Model']
        desktop_update.cpu = request.form['CPU']
        desktop_update.ram = request.form['RAM']
        desktop_update.storage = request.form['Storage']
        desktop_update.operating_system = request.form['Operating_System']
        desktop_update.mac_address = request.form['Mac_address']
        desktop_update.location = request.form.get('Location')
        try:
            db.session.commit()
            return redirect('/desktops')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update_desktop.html', desktop_update=desktop_update)

@main.route('/update_mobile_phone/<int:id>', methods=['POST', 'GET'])
@login_required
def update_mobile_phone(id):
    mobile_phone_update = Mobile_Phone.query.get_or_404(id)
    if request.method == "POST":
        mobile_phone_update.manufactor = request.form['Manufacturer']
        mobile_phone_update.model = request.form['Model']
        mobile_phone_update.display = request.form['Display']
        mobile_phone_update.cpu = request.form['CPU']
        mobile_phone_update.storage = request.form['Storage']
        mobile_phone_update.operating_system = request.form['Operating_System']
        mobile_phone_update.location = request.form.get('Location')
        try:
            db.session.commit()
            return redirect('/mobile_phones')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update_mobile_phone.html', mobile_phone_update=mobile_phone_update)


########################## DELETE FUNCTIONS ##########################

@main.route('/delete_laptop/<int:id>')
@login_required
def delete_laptop(id):
    laptop_delete = Laptops.query.get_or_404(id)
    try:
        db.session.delete(laptop_delete)
        db.session.commit()
        return redirect('/laptops')
    except:
        return "There was an issue deleting that laptop im sorry :("

@main.route('/delete_desktop/<int:id>')
@login_required
def delete_desktop(id):
    desktop_delete = Desktops.query.get_or_404(id)
    try:
        db.session.delete(desktop_delete)
        db.session.commit()
        return redirect('/desktops')
    except:
        return "There was an issue deleting that laptop im sorry :("

@main.route('/delete_mobile_phone/<int:id>')
@login_required
def delete_mobile_phone(id):
    mobile_phone_delete = Mobile_Phone.query.get_or_404(id)
    try:
        db.session.delete(mobile_phone_delete)
        db.session.commit()
        return redirect('/mobile_phones')
    except:
        return "There was an issue deleting that laptop im sorry :("

@main.route('/delete_sim_card/<int:id>')
@login_required
def delete_sim_card(id):
    sim_card_delete = SimCards.query.get_or_404(id)
    try:
        db.session.delete(sim_card_delete)
        db.session.commit()
        return redirect('/sim_cards')
    except:
        return "There was an issue deleting that laptop im sorry :("