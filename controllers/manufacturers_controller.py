from models.manufacturers import Manufacturers
from flask import Flask, render_template, request,redirect
from repositories import inventory_repository, manufacturer_repository
import repositories.inventory_repository as inventory_repository
import repositories.manufacturer_repository as manufacturer_repository
from models.inventory import Inventory

from flask import Blueprint
manufacturer_blueprint = Blueprint("inventory",__name__)

@manufacturer_blueprint.route("/inventory/manufacturer")
def inventory():
    inventory = inventory_repository.select_all()
    return render_template("inventory/index.html",all_inventory = inventory)