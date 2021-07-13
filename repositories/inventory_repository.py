from db.run_sql import run_sql
from models.inventory import Inventory
from models.manufacturers import Manufacturers
import repositories.manufacturer_repository as manufacturer_repository

def save(inventory):
    sql =  "INSERT INTO inventory (item_name, manufacturers_id,description,stock_quantity,buying_cost,selling_cost) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [inventory.item_name, inventory.manufacturer.id, inventory.description, inventory.stock_quantity, inventory.buying_cost, inventory.selling_cost]
    results = run_sql(sql,values)
    id = results[0]['id']
    inventory.id = id
    return inventory

def select_all():
    inventory = []

    sql = "SELECT * FROM inventory"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        inventory = Inventory(row['item_name'], manufacturer, row['description'], row['stock_quantity'], row['buying_cost'],row['selling_cost'],row['id'])
        inventory.append(inventory)
    return inventory

def select(id):
    inventory = None
    sql = "SELECT * FROM inventory WHERE id = %s"
    values= [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        inventory = Inventory(result['item_name'], manufacturer, result['description'], result['stock_quantity'], result['buying_cost'],result['selling_cost'],result['id'])
    return inventory

def delete(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql,values)


def update(inventory):
    sql = "UPDATE inventory SET(item_name, manufacturer,description,stock_quantity,buying_cost,selling_cost) = (%s,%s,%s,%s,%s,%s) WHERE id = %s "
    values = [inventory.item_name, inventory.manufacturer, inventory.description, inventory.stock_quantity, inventory.buying_cost, inventory.selling_cost]
    run_sql(sql, values)
    
