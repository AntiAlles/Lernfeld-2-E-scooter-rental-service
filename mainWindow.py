from ctypes import alignment
from data_class import *
from tkinter import *




db.connect()
db.create_tables([Scooters, Calculations])

if not Scooters.select().where(Scooters.name == 'Tier S').exists():
    Scooters.create(name='Tier S', price_distance=20, price_time=50, unlock_fee=1.33)
if not Scooters.select().where(Scooters.name == 'Tier M').exists():
    Scooters.create(name='Tier M', price_distance=30, price_time=77, unlock_fee=2.33)
if not Scooters.select().where(Scooters.name == 'Tier L').exists():
    Scooters.create(name='Tier L', price_distance=40, price_time=100, unlock_fee=0.20)

#Main Vars
scooters = Scooters.select()
scooter_names = map(lambda scooter: scooter.name, scooters)

fenster = Tk()
fenster.rowconfigure(0,weight=2)
fenster.rowconfigure(1,weight=1)
fenster.rowconfigure(2,weight=1)
fenster.title("ScooTeC")
fenster.geometry("420x500")
fenster.minsize(width=420, height=500)


# Info Label
label = Label(fenster, text="ScooTeq\nProgram to calculate the Price for your Duration or Distance driven.")

#button variables
clicked = StringVar()
clicked.set("Select a skuter")

price_time = StringVar()
price_distance = StringVar()
price_unlock_fee = StringVar()

def scooter_trace(var, index, mode):
    s = Scooters.get(Scooters.name == clicked.get())
    price_time.set(s.price_time)
    price_distance.set(s.price_distance)
    price_unlock_fee.set(s.unlock_fee)
    prices.configure(text=f'Verschuldung / Sekunde: {price_time.get()}€\nVerschuldung / Distanz: {price_distance.get()}€\nVerschuldung / Schlechte Lebensentscheidung: {price_unlock_fee.get()}€')

prices = Label(fenster, text="")

clicked.trace_variable("w", scooter_trace)

def calculate_price():
    s = Scooters.get(Scooters.name == clicked.get())
    price = (s.price_time if type_radio.get() == "time" else s.price_distance) * int(input_verschuldung.get()) + s.unlock_fee
    Calculations.create(scooter=s.id, is_distance_calculation=type_radio.get() == "distance", value=price, include_unlock_fee=True)

    l_calculation.configure(text=f'{price}€')


# Widgets
b_kategories = OptionMenu(fenster, clicked, *scooter_names)
b_exit = Button(fenster, text="Exit", command="exit")
b_calculate= Button(fenster, text="RECHNE", command=calculate_price)

input_verschuldung = Entry(fenster)

type_radio = StringVar()
type_radio.set("time")
t_select = Radiobutton(fenster, text="Time", variable=type_radio, value="time")
d_select = Radiobutton(fenster, text="Distance", variable=type_radio, value="distance")
l_calculation = Label(fenster, text="", font=("Comic Sans MS", 20))

#Widget builder
label.grid(row=0, columnspan=2)
b_kategories.grid(row=1)
prices.grid(row=1, column=1)
t_select.grid(row=2, column=0)
d_select.grid(row=2, column=1)
input_verschuldung.grid(row=3)
b_calculate.grid(row=3, column=1)
l_calculation.grid(row=4)
b_exit.grid(row=5)


fenster.mainloop()

print("Bye")