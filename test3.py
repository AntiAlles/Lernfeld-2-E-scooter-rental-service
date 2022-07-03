from tkinter import *

fenster = Tk()

fenster.title("Databank_KrautundRüben")
fenster.geometry("500x400")
fenster.minsize(width=500, height=400)
frame= Frame(fenster)

# root.resizeable(width=False, height=False)


options = [
    "kunde",
    "bestellung",
    "lieferant",
    "zutat",
    "bestellungszutat"
]

options2 = [
    "kunde",
    "bestellung",
    "lieferant",
    "zutat",
    "bestellungszutat"
]

options3 = [
    "kunde",
    "bestellung",
    "lieferant",
    "zutat",
    "bestellungszutat"
]

# Create Label
label = Label(fenster, text=" ")


def exit():
    exit()


label1 = Label(fenster,
               text="\n\nWelcome to the Databank of Kraut und Rüben\n\n"
					"Here you can have look at the different kategories of the database Kraut und Rüben\n"
					"you can take a look at different tabels or even save them as a textdokument.\n.\n"
					"To get started select a kategory and press the button\n")

clicked = StringVar()
clicked.set("1.Kategories")
clicked2 = StringVar()
clicked2.set("2.Tabels")

clicked3 = StringVar()
clicked3.set("3.Textdocs")


def show():
    label.config(text=clicked.get())


b_kategories = OptionMenu(frame, clicked, *options)
b_tabels = OptionMenu(frame, clicked2, *options2)
b_textdoc = OptionMenu(frame, clicked3, *options3)
b_exit = Button(frame, text="Exit", command="exit")
button = Button(frame, text="click Me", command=show)

label = Label(fenster, text=" ")

label1.pack(anchor="n")
b_kategories.pack(side="left")
b_tabels.pack(side="left")
b_textdoc.pack(side="left")
b_exit.pack(side="left")

button.pack(side="left")
label.pack(anchor="center")

fenster.mainloop()

print("Bye")
