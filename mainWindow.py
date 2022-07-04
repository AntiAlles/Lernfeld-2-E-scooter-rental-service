from ctypes import alignment
from data_class import *
from tkinter import *



#Database Connector with Variable from data_class.py
db.connect()
db.create_tables([Scooters, Calculations])

#Checks if the Database entries exist and if not creates them.
if not Scooters.select().where(Scooters.name == 'Tier S').exists():
    Scooters.create(name='Tier S', price_distance=10, price_time=0.29, unlock_fee=1.33)
if not Scooters.select().where(Scooters.name == 'Tier M').exists():
    Scooters.create(name='Tier M', price_distance=25, price_time=0.49, unlock_fee=2.33)
if not Scooters.select().where(Scooters.name == 'Tier L').exists():
    Scooters.create(name='Tier L', price_distance=40, price_time=0.99, unlock_fee=0.20)

#Database Var and Scooter Mapping
scooters = Scooters.select()
scooter_names = map(lambda scooter: scooter.name, scooters)

#Window configuration
fenster = Tk()
fenster.title("ScooTeC")
fenster.geometry("600x300")
fenster.minsize(width=500, height=300)

#Column Size/weight
fenster.columnconfigure(0,weight=2)
fenster.columnconfigure(1,weight=1)
fenster.columnconfigure(2,weight=1)

#Info Label
label = Label(fenster, text="ScooTeq\nProgram to calculate the Price for your Duration or Distance driven.")

#button variable configuration
clicked = StringVar()
clicked.set("Select a Scooter")
price_time = StringVar()
price_distance = StringVar()
price_unlock_fee = StringVar()

#button functions
def scooter_trace(var, index, mode):
    s = Scooters.get(Scooters.name == clicked.get())
    price_time.set(s.price_time)
    price_distance.set(s.price_distance)
    price_unlock_fee.set(s.unlock_fee)
    prices.configure(text=f'Price / per Minute: {price_time.get()}€\n Price / Distance: {price_distance.get()}€\n Price / Unlock Fee: {price_unlock_fee.get()}€')

prices = Label(fenster, text="")

clicked.trace_variable("w", scooter_trace)

def calculate_price():
    s = Scooters.get(Scooters.name == clicked.get())
    price = (s.price_time if type_radio.get() == "time" else s.price_distance) * int(input_verschuldung.get()) + s.unlock_fee
    Calculations.create(scooter=s.id, is_distance_calculation=type_radio.get() == "distance", value=price, include_unlock_fee=True)

    l_calculation.configure(text=f'{price}€')


#Configurations for the buttons and their corresponding functions
b_kategories = OptionMenu(fenster, clicked, *scooter_names)
b_exit = Button(fenster, text="Exit", command="exit")
b_calculate= Button(fenster, text="Calculate", command=calculate_price)
input_verschuldung = Entry(fenster)
type_radio = StringVar()
type_radio.set("time")
t_select = Radiobutton(fenster, text="Time", variable=type_radio, value="time")
d_select = Radiobutton(fenster, text="Distance", variable=type_radio, value="distance")
l_calculation = Label(fenster, text="", font=(20))

#Places the buttons and widgets inside the window
label.grid(row=0, column=1, columnspan=1)
prices.grid(row=1, column=1)
b_kategories.grid(row=2, column=0)
t_select.grid(row=2, column=1)
d_select.grid(row=2, column=2)
input_verschuldung.grid(row=3, column=1)
b_calculate.grid(row=3, column=2)
l_calculation.grid(row=4, column=1)
b_exit.grid(row=300, column=2, sticky=S)


fenster.mainloop()

print("Bye")