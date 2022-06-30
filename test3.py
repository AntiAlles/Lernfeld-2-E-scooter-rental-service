import tkinter

fenster =tkinter.Tk()

fenster.title("Databank_KrautundRüben")
fenster.geometry("500x400")
fenster.minsize(width=500, height=400)
#root.resizeable(width=False, height=False)



label1 = tkinter.Label(fenster,text="\n\nWelcome to the Databank of Kraut und Rüben\n\n"
                                    "Here you can have look at the different kategories of the database Kraut und Rüben\n"
                                    "you can take a look at different tabels or even save them as a textdokument.\n.\n"
                                    "To get started select a kategory and press the button\n")

b_kategories = tkinter.Button(fenster, text="1.Kategories")
b_tabels = tkinter.Button(fenster, text="2.Tabels")
b_textdoc =tkinter.Button(fenster, text="3.Texdocument")
b_exit =tkinter.Button(fenster, text="Exit")



label1.pack()
b_kategories.pack(padx=20, pady=5, side='left', expand= 1)
b_tabels.pack(padx=20, pady=5, side='left', expand= 1)
b_textdoc.pack(padx=20, pady=5, side='left', expand= 1)
b_exit.pack(padx=20, pady=5, side='left', expand= 1)




fenster.mainloop()

print("Bye")