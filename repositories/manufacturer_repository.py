from db.run_sql import run_sql
from models.manufacturers import Manufacturers
from models.inventory import Inventory

def save(manufacturer):
    sql = "INSERT INTO manufacturers (company_name, description) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.company_name, manufacturer.description]
    results = run_sql(sql, values)
    id = results [0]['id']
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturers(row['company_name'], row['description'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql="SELECT * FROM manufacturers WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturers(result['company_name'],result['description'],result['id'])
    return manufacturer

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (company_name, description) = (%s,%s) WHERE id = %s"
    values = [manufacturer.company_name, manufacturer.description, manufacturer.id]
    run_sql(sql,values)


def inventory(manufacturer):
    inventory = []

    sql = "SELECT * FROM inventory WHERE manufacturer_id = %s"
    values=[manufacturer.id]
    results= run_sql(sql,values)

    for row in results:
        inventory = Inventory(row['item_name'],row['manufacturer_id'],row['description'],row['stock_quantity'],row['buying_cost'],row['selling_cost'],row['id'])
        inventory.append(inventory)
    return inventory