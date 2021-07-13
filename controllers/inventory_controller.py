from flask import Flask, render_template, request,redirect
from repositories import inventory_repository
import repositories.inventory_repository as inventory_repository
from models.inventory import Inventory


from flask import Blueprint

inventory_blueprint = Blueprint("inventory",__name__)


@inventory_blueprint.route("/inventory")
def inventory():
    inventory = inventory_repository.select_all()
    return render_template("inventory/index.html",all_inventory = inventory)


