from urllib import request
import sys
from importlib import reload
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import func

from .__init__ import db

from .models.site_models import *

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
    desktop_count = Desktops.query.count()
    tablet_count = Tablets.query.count()
    mobile_phone_count = Mobile_Phone.query.count()
    peripherals_count = Peripherals.query.with_entities(func.sum(Peripherals.amount).label('total')).first().total
    sim_card_count = SimCards.query.with_entities(func.sum(SimCards.amount).label('total')).first().total
    tools_count = Tools.query.with_entities(func.sum(Tools.amount).label('total')).first().total
    accessory_count = Accessories.query.with_entities(func.sum(Accessories.amount).label('total')).first().total
    site_objectives = Site_Objectives.query
    return render_template('dashboard.html',name=current_user.name, 
    laptop_count=laptop_count, laptop_assigned=laptop_assigned, 
    laptop_unassigned=laptop_unassigned, 
    desktop_count=desktop_count,
    tablet_count=tablet_count, 
    mobile_phone_count=mobile_phone_count,
    peripherals_count=peripherals_count, 
    sim_card_count=sim_card_count,
    tools_count=tools_count, 
    accessory_count = accessory_count,
    site_objectives=site_objectives)

@main.route('/site_objectives', methods=['POST', 'GET'])
@login_required
def site_objectives():
    if request.method == "POST":
        objective = request.form['Objective']
        try:
            new_objective = Site_Objectives(Todofield=objective)
            db.session.add(new_objective)
            db.session.commit()
            return redirect('/dashboard')
        except:
            return "There was an issue adding that objective im sorry :("

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

@main.route('/tablets', methods=['POST', 'GET'])
@login_required
def tablets():
    if request.method == "POST":
        new_tablet_name = request.form['Name']
        new_tablet_manufacturer = request.form['Manufacturer']
        new_tablet_model = request.form['Model']
        new_tablet_cpu = request.form['CPU']
        new_tablet_ram = request.form['RAM']
        new_tablet_storage = request.form['Storage']
        new_tablet_OS = request.form['Operating_System']
        new_tablet_ma = request.form['Mac_address']
        new_tablet_location = request.form.get('Location')
        new_tablet_assigned = request.form.get('assigned')
        new_tablet_assigned_to = request.form['Assigned_to']
        try:
            new_tablet = Tablets(name=new_tablet_name, manufactor=new_tablet_manufacturer, 
            model=new_tablet_model, cpu=new_tablet_cpu, ram=new_tablet_ram, storage=new_tablet_storage, 
            operating_system=new_tablet_OS, mac_address = new_tablet_ma, location=new_tablet_location,
            assigned=new_tablet_assigned, assigned_to=new_tablet_assigned_to)
            db.session.add(new_tablet)
            db.session.commit()
            return redirect('/tablets')
        except:
            "There was an error adding your data"
    else:
        tablet = Tablets.query
        return render_template('tablets.html', tablet=tablet)

@main.route('/peripherals', methods=['POST', 'GET'])
@login_required
def peripherals():
    if request.method == "POST":
        new_peripheral_form_type = request.form.get('Type')
        new_peripheral_form_manufacturer = request.form['Manufacturer']
        new_peripheral_form_model = request.form['Model']
        new_peripheral_form_amount = request.form['Amount']
        new_peripheral_form_location = request.form.get('Location')
        try:
            new_peripheral = Peripherals(type=new_peripheral_form_type,
            manufactor = new_peripheral_form_manufacturer,
            model = new_peripheral_form_model,
            amount = new_peripheral_form_amount, 
            location=new_peripheral_form_location)
            db.session.add(new_peripheral)
            db.session.commit()
            return redirect('/peripherals')
        except:
            "There was an error adding your data"
    else:
        peripherals = Peripherals.query
        return render_template('peripherals.html', peripherals=peripherals)

@main.route('/tools', methods=['POST', 'GET'])
@login_required
def tools():
    if request.method == "POST":
        new_tool_form_name = request.form['Name']
        new_tool_form_type = request.form.get('Type')
        new_tool_form_manufacturer = request.form['Manufacturer']
        new_tool_form_amount = request.form['Amount']
        new_tool_form_location = request.form.get('Location')
        try:
            new_tool = Tools(name=new_tool_form_name,
            type = new_tool_form_type,
            manufacturer = new_tool_form_manufacturer,
            amount = new_tool_form_amount,
            location = new_tool_form_location)
            db.session.add(new_tool)
            db.session.commit()
            return redirect('/tools')
        except:
            "There was an error adding your data"
    else:
        tools = Tools.query
        return render_template('tools.html', tools=tools)

@main.route('/accessories', methods=['POST', 'GET'])
@login_required
def accessories():
    if request.method == "POST":
        new_accessory_form_name = request.form['Name']
        new_accessory_form_type = request.form.get('Type')
        new_accessory_form_manufacturer = request.form['Manufacturer']
        new_accessory_form_amount = request.form['Amount']
        new_accessory_form_location = request.form.get('Location')
        try:
            new_accessory = Accessories(name=new_accessory_form_name,
            type = new_accessory_form_type,
            manufacturer = new_accessory_form_manufacturer,
            amount = new_accessory_form_amount,
            location = new_accessory_form_location)
            db.session.add(new_accessory)
            db.session.commit()
            return redirect('/accessories')
        except:
            "There was an error adding your data"
    else:
        accessories = Accessories.query
        return render_template('accessories.html', accessories=accessories)

########################## UPDATE FUNCTIONS ##########################

@main.route('/update_laptop/<int:id>', methods=['POST', 'GET'])
@login_required
def update_laptop(id):
    laptop_update = Laptops.query.get_or_404(id)
    if request.method == "POST":
        laptop_update.name = request.form['Name']
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

@main.route('/update_tablet/<int:id>', methods=['POST', 'GET'])
@login_required
def update_tablet(id):
    tablet_update = Tablets.query.get_or_404(id)
    if request.method == "POST":
        tablet_update.model = request.form['Name']
        tablet_update.manufactor = request.form['Manufacturer']
        tablet_update.model = request.form['Model']
        tablet_update.cpu = request.form['CPU']
        tablet_update.ram = request.form['RAM']
        tablet_update.storage = request.form['Storage']
        tablet_update.operating_system = request.form['Operating_System']
        tablet_update.mac_address = request.form['Mac_address']
        tablet_update.location = request.form.get('Location')
        tablet_update.assigned = request.form.get('assigned')
        tablet_update.assigned_to = request.form['Assigned_to']
        try:
            db.session.commit()
            return redirect('/tablets')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update_tablet.html', tablet_update=tablet_update)

@main.route('/update_mobile/<int:id>', methods=['POST', 'GET'])
@login_required
def update_mobile(id):
    mobile_update = Mobile_Phone.query.get_or_404(id)
    if request.method == "POST":
        mobile_update.manufactor = request.form['Manufacturer']
        mobile_update.model = request.form['Model']
        mobile_update.display = request.form['Display']
        mobile_update.cpu = request.form['CPU']
        mobile_update.storage = request.form['Storage']
        mobile_update.operating_system = request.form['Operating_System']
        mobile_update.location = request.form.get('Location')
        try:
            db.session.commit()
            return redirect('/mobile_phones')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update_mobile.html', mobile_update=mobile_update)

@main.route('/update_peripheral/<int:id>', methods=['POST', 'GET'])
@login_required
def update_peripheral(id):
    peripheral_update = Peripherals.query.get_or_404(id)
    if request.method == "POST":
        peripheral_update.type = request.form.get('Type')
        peripheral_update.manufactor = request.form['Manufacturer']
        peripheral_update.model = request.form['Model']
        peripheral_update.location = request.form.get('Location')
        peripheral_update.amount = request.form['Amount']
        peripheral_update.notes = request.form['Notes']
        try:
            db.session.commit()
            return redirect('/peripherals')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update_peripheral.html', peripheral_update=peripheral_update)

@main.route('/update_tool/<int:id>', methods=['POST', 'GET'])
@login_required
def update_tool(id):
    tool_update = Tools.query.get_or_404(id)
    if request.method == "POST":
        tool_update.name = request.form['Name']
        tool_update.type = request.form.get('Type')
        tool_update.manufactor = request.form['Manufacturer']
        tool_update.location = request.form.get('Location')
        tool_update.amount = request.form['Amount']
        tool_update.notes = request.form['Notes']
        try:
            db.session.commit()
            return redirect('/tools')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update_tool.html', tool_update=tool_update)

@main.route('/update_accessory/<int:id>', methods=['POST', 'GET'])
@login_required
def update_accessory(id):
    accessory_update = Accessories.query.get_or_404(id)
    if request.method == "POST":
        accessory_update.name = request.form['Name']
        accessory_update.type = request.form.get('Type')
        accessory_update.manufactor = request.form['Manufacturer']
        accessory_update.location = request.form.get('Location')
        accessory_update.amount = request.form['Amount']
        accessory_update.notes = request.form['Notes']
        try:
            db.session.commit()
            return redirect('/accessories')
        except:
            return "There was an issue updating that laptop 404 IM SO SORRY! I SUCK :("
    else:
        return render_template('update_accessory.html', accessory_update=accessory_update)


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
        return "There was an issue deleting that desktop im sorry :("

@main.route('/delete_mobile_phone/<int:id>')
@login_required
def delete_mobile_phone(id):
    mobile_phone_delete = Mobile_Phone.query.get_or_404(id)
    try:
        db.session.delete(mobile_phone_delete)
        db.session.commit()
        return redirect('/mobile_phones')
    except:
        return "There was an issue deleting that mobile im sorry :("

@main.route('/delete_sim_card/<int:id>')
@login_required
def delete_sim_card(id):
    sim_card_delete = SimCards.query.get_or_404(id)
    try:
        db.session.delete(sim_card_delete)
        db.session.commit()
        return redirect('/sim_cards')
    except:
        return "There was an issue deleting that sim-card im sorry :("

@main.route('/delete_tablet/<int:id>')
@login_required
def delete_tablet(id):
    tablet_delete = Tablets.query.get_or_404(id)
    try:
        db.session.delete(tablet_delete)
        db.session.commit()
        return redirect('/tablets')
    except:
        return "There was an issue deleting that tablet im sorry :("

@main.route('/delete_peripheral/<int:id>')
@login_required
def delete_peripheral(id):
    peripheral_delete = Peripherals.query.get_or_404(id)
    try:
        db.session.delete(peripheral_delete)
        db.session.commit()
        return redirect('/peripherals')
    except:
        return "There was an issue deleting that Peripheral im sorry :("

@main.route('/delete_tool/<int:id>')
@login_required
def delete_tool(id):
    tool_delete = Tools.query.get_or_404(id)
    try:
        db.session.delete(tool_delete)
        db.session.commit()
        return redirect('/tools')
    except:
        return "There was an issue deleting that Tool im sorry :("

@main.route('/delete_accessory/<int:id>')
@login_required
def delete_accessory(id):
    accessory_delete = Accessories.query.get_or_404(id)
    try:
        db.session.delete(accessory_delete)
        db.session.commit()
        return redirect('/accessories')
    except:
        return "There was an issue deleting that Accessory im sorry :("

@main.route('/delete_objective/<int:id>')
@login_required
def delete_objective(id):
    objective_delete = Site_Objectives.query.get_or_404(id)
    try:
        db.session.delete(objective_delete)
        db.session.commit()
        return redirect('/dashboard')
    except:
        return "There was an issue deleting that Accessory im sorry :("