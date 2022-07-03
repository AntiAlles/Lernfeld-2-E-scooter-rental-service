from data_class import bfunctions
from tkinter import *

fenster = Tk()
fenster.rowconfigure(0,weight=2)
fenster.rowconfigure(1,weight=1)
fenster.rowconfigure(2,weight=1)
fenster.title("Databank_KrautundRüben")
fenster.geometry("500x400")
fenster.minsize(width=500, height=400)

options = [
    "kunde",
    "bestellung",
    "lieferant",
    "zutat",
    "bestellungszutat"
]

options2 = [
    "CUNT",
    "C C",
    "U U",
    "N N",
    "T T"
]

options3 = [
    "kunde",
    "bestellung",
    "lieferant",
    "zutat",
    "bestellungszutat"
]

# Create Label
label = Label(fenster, text="\n\nWelcome to the Databank of Kraut und Rüben\n\n"
                            "Here you can have look at the different kategories of the database Kraut und Rüben\n"
                            "you can take a look at different tabels or even save them as a textdokument.\n.\n"
                            "To get started select a kategory and press the button\n")

clicked = StringVar()
clicked.set("1.Kategories")
clicked2 = StringVar()
clicked2.set("2.Tabels")
clicked3 = StringVar()
clicked3.set("3.Textdocs")

b_kategories = OptionMenu(fenster, clicked, *options)
b_tabels = OptionMenu(fenster, clicked2, *options2)
b_textdoc = OptionMenu(fenster, clicked3, *options3)
b_exit = Button(fenster, text="Exit", command="exit")
button = Button(fenster, text="click Me")

label.grid(padx=20, columnspan=3)
b_kategories.grid(row=1)
b_tabels.grid(row=1,column=1)
b_textdoc.grid(row=1, column=2)
b_exit.grid(row=2, column=2)

fenster.mainloop()

print("Bye")