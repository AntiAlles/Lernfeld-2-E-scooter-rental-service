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


scooters = Scooters.select()

fenster = Tk()
fenster.rowconfigure(0,weight=2)
fenster.rowconfigure(1,weight=1)
fenster.rowconfigure(2,weight=1)
fenster.title("ScooTeC")
fenster.geometry("500x400")
fenster.minsize(width=500, height=400)


# Info Label
label = Label(fenster, text="ScooTeq\n Program to calculate the Price for your Duration or Distance driven.")

#button variables
clicked = StringVar()
clicked.set("1.Kategories")
clicked2 = StringVar()
clicked2.set("2.Tabels")
clicked3 = StringVar()
clicked3.set("3.Textdocs")

#Widgets
b_kategories = OptionMenu(fenster, clicked, *options)
b_tabels = OptionMenu(fenster, clicked2, *options2)
b_textdoc = OptionMenu(fenster, clicked3, *options3)
b_exit = Button(fenster, text="Exit", command="exit")
button = Button(fenster, text="click Me", command="show")

#Widget builder
label.grid(padx=20, columnspan=3)
b_kategories.grid(row=1)
b_tabels.grid(row=1,column=1)
b_textdoc.grid(row=1, column=2)
button.grid(row=2,column=1)
b_exit.grid(row=2, column=2)

fenster.mainloop()

print("Bye")