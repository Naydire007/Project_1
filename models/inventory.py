class Inventory:
    def __init__(self, item_name, manufacturer, description,stock_quantity,buying_cost,selling_cost,id=None):
        self.item_name = item_name
        self.manufacturer = manufacturer
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_cost = selling_cost
        self.id = id

 
    