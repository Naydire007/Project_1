import pdb
from models.inventory import Inventory
from models.manufacturers import Manufacturers

import repositories.manufacturer_repository as manufacturer_repository
import repositories.inventory_repository as inventory_repository

inventory_repository.delete_all()
manufacturer_repository.delete_all()


manufacturer1 = Manufacturers("Magic Life","Useful product for your quests")
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturers("Aqua Vitae", "Saving you again")
manufacturer_repository.save(manufacturer2)

something=manufacturer_repository.select_all()

item1 = Inventory("Healing potion", manufacturer1, "Heals superficial wounds", 3, 20,30)
inventory_repository.save(item1)
item2 = Inventory("Resurrect", manufacturer2, "Heals superficial wounds", 1, 25,50)
inventory_repository.save(item2)

pdb.set_trace()