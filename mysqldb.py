import mysql.connector
import tkinter


#Aufbau einer Verbindung
db = mysql.connector.connect(
  host="127.0.0.1", # Servername
  user="root", # Benutzername
  password="", # Passwort
  database="krautundrueben"
)
fenster= tkinter.Tk()


index = ['0', '1.Kategories','2.Tabels', '3.Textdocs', '4.Exit']

print("Welcome to the Database of Kraut und Rüben")
print("")
print("Here you can have look at the different kategories of the database,")
print("you can take a look at different tabels or even save them as a textdokument.")
print("")
print("To select your kategory press the number and enter")
print("What are you intrested in")

print(index[1:5])
select= int(input(""))
selector= index[select]
print(selector + "is selected")


while int(select) != 4:

    if int(select) == 1 :
        operator = ['kunde', 'bestellung', 'lieferant', 'zutat', 'bestellungszutat']
        nutzereingabe = ""

        while nutzereingabe != operator:

            nutzereingabe2 = input("What kategorie do you want to see? ")
            print("")
            help = ['help', 'h']

            if nutzereingabe2 in operator:
                break

            if nutzereingabe2 in help:
                print(" ")
                print("Those are all kategories")
                print("kunde, lieferant, bestellung, zutat, bestellungszutat")

            else:
                print("For examples write h or help")

        mycursor = db.cursor()

        mycursor.execute("DESCRIBE " + nutzereingabe2)

        for x in mycursor:
            print(x)
        break







    if int(select) == 2 :

        operator = ['kunde', 'bestellung', 'lieferant', 'zutat', 'bestellungszutat']
        nutzereingabe = ""

        while nutzereingabe != operator:

            nutzereingabe2 = input("Select a kategorie to see the data? ")
            print("")
            help = ['help', 'h']

            if nutzereingabe2 in operator:
                break

            if nutzereingabe2 in help:
                print("")
                print("Those are all kategories")
                print("kunde, lieferant, bestellung, zutat, bestellungszutat")

            else:
                print("For examples write h or help")

        mycursor = db.cursor()

        mycursor.execute("SELECT * FROM " + nutzereingabe2)

        for x in mycursor:
            print(x)
        break





    if int(select) == 3:

        operator = ['kunde', 'bestellung', 'lieferant', 'zutat', 'bestellungszutat']
        nutzereingabe = ""

        while nutzereingabe != operator:

            nutzereingabe2 = input("Select a kategorie to see the data? ")
            print("")
            help = ['help', 'h']

            if nutzereingabe2 in operator:
                break

            if nutzereingabe2 in help:
                print("")
                print("Those are all kategories")
                print("kunde, lieferant, bestellung, zutat, bestellungszutat")

            else:
                print("For examples write h or help")

        mycursor = db.cursor()
        kategorie =[]
        datei = open(str(nutzereingabe2) + ".txt", "w")

        mycursor.execute("DESCRIBE " + nutzereingabe2)
        for x in mycursor:
            kategorie.append(x[0])


        mycursor.execute("SELECT * FROM " + nutzereingabe2)
        tabelle = []
        for x in mycursor:
            tabelle.append(x)

        datei.write(str(kategorie))
        for x in range(len(tabelle)):
            datei.write("\r\n"+ str(tabelle[x]))

        datei.close()

        print("The file " + str(nutzereingabe2) + ".txt has been created")
        print("")

        break

    break


print("Bye")