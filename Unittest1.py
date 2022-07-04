import unittest 
from mainWindow import *

class TestCalculation(unittest.TestCase):
    def calculate_price():
        s = Scooters.get(Scooters.name == clicked.get())
        price = (s.price_time if type_radio.get() == "time" else s.price_distance) * int(input_verschuldung.get()) + s.unlock_fee
        Calculations.create(scooter=s.id, is_distance_calculation=type_radio.get() == "distance", value=price, include_unlock_fee=True)

        l_calculation.configure(text=f'{price}€')