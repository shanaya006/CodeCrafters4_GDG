import random

def predict_disaster():
    disasters = ['flood', 'earthquake', 'cyclone', 'none']
    disaster = random.choice(disasters)
    severity = random.randint(1, 10)
    return disaster, severity
