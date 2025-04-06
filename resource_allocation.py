def allocate_resources(disaster, severity):
    if disaster == 'none':
        return {}

    base = {
        'food_kits': 100,
        'water_bottles': 200,
        'med_kits': 50,
        'tents': 30
    }

    return {item: qty * severity for item, qty in base.items()}

