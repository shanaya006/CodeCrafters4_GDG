inventory_db = {
    'boats': 50,
    'food': 5000,
    'med_kits': 2000,
    'excavators': 20,
    'blankets': 1000,
    'tents': 300
}

def check_inventory(allocation):
    shortages = {}
    for item, qty in allocation.items():
        available = inventory_db.get(item, 0)
        if available < qty:
            shortages[item] = qty - available
    return shortages

def update_inventory(allocation):
    for item, qty in allocation.items():
        if item in inventory_db:
            inventory_db[item] -= qty
