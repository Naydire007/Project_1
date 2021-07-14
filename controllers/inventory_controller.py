from models.manufacturers import Manufacturers
from flask import Flask, render_template, request,redirect
from repositories import inventory_repository, manufacturer_repository
import repositories.inventory_repository as inventory_repository
import repositories.manufacturer_repository as manufacturer_repository
from models.inventory import Inventory


from flask import Blueprint

inventory_blueprint = Blueprint("inventory",__name__)


@inventory_blueprint.route("/inventory")
def inventory():
    inventory = inventory_repository.select_all()
    return render_template("inventory/index.html",all_inventory = inventory)

@inventory_blueprint.route("/inventory/new")
def new_item():
    manufacturer= manufacturer_repository.select_all()
    return render_template("inventory/new.html", all_manufacturers = manufacturer)

@inventory_blueprint.route("/inventory", methods=["POST"])
def create_inventory():
        item_name = request.form['item_name']
        manufacturer = manufacturer_repository.select(request.form['manufacturers_id'])
        description = request.form['description']
        stock_quantity = request.form['stock_quantity']
        buying_cost = request.form['buying_cost']
        selling_cost = request.form['selling_cost']
        inventory = Inventory(item_name,manufacturer,description,stock_quantity,buying_cost,selling_cost)
        inventory_repository.save(inventory)
        return redirect('/inventory')


# Show
@inventory_blueprint.route("/inventory/<id>", methods=['GET'])
def show_inventory(id):
    inventory = inventory_repository.select(id)
    return render_template('inventory/show.html',inventory = inventory)


# EDIT
@inventory_blueprint.route("/inventory/<id>/edit", methods = ['GET'])
def edit_inventory(id):
    inventory = inventory_repository.select(id)
    manufacturer = manufacturer_repository.select_all()
    return render_template('inventory/edit.html', inventory=inventory, all_manufacturers = manufacturer)

# UPDATE
@inventory_blueprint.route("/inventory/<id>", methods=['POST'])
def update_inventory(id):
        item_name = request.form['item_name']
        manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
        description = request.form['description']
        stock_quantity = request.form['stock_quantity']
        buying_cost = request.form['buying_cost']
        selling_cost = request.form['selling_cost']
        inventory = Inventory(item_name,manufacturer,description,stock_quantity,buying_cost,selling_cost)
        inventory_repository.update(inventory)
        return redirect('/inventory')


# DELETE
@inventory_blueprint.route("/inventory/<id>/delete", methods=['POST'])
def delete_inventory(id):
    inventory_repository.delete(id)
    return redirect('/inventory')