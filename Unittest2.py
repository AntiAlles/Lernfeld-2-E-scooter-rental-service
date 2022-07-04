import unittest 
from mainWindow import *

class TestCalculation(unittest.TestCase):
    def scooter_trace(var, index, mode):
        s = Scooters.get(Scooters.name == clicked.get())
        price_time.set(s.price_time)
        price_distance.set(s.price_distance)
        price_unlock_fee.set(s.unlock_fee)
        prices.configure(text=f'Price / per Minute: {price_time.get()}€\n Price / Distance: {price_distance.get()}€\n Price / Unlock Fee: {price_unlock_fee.get()}€')
