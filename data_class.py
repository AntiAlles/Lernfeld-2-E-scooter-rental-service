from tkinter import *
from peewee import *
import datetime

db = SqliteDatabase('skutek.db')



class Scooters(Model):
    id = AutoField()
    name = CharField()
    price_distance = DoubleField()
    price_time = DoubleField()
    unlock_fee = DoubleField()

    class Meta:
        database = db

class Calculations(Model):
    id = AutoField()
    scooter = ForeignKeyField(Scooters)
    timestamp = DateTimeField(default=datetime.datetime.now)
    is_distance_calculation = BooleanField()
    value = DoubleField()
    include_unlock_fee = BooleanField()

    class Meta:
        database = db
        





class bfunctions():

    def exit():
        exit()
    """Function to exit the program per Button"""
    
