#a) Die vier Hauptdatentypen in Python sind:

#Ganzzahl (int), Beispiel: 42
#Gleitkommazahl (float), Beispiel: 3.14
#Zeichenkette (str), Beispiel: "Hallo Welt"
#Boolescher Wert (bool), Beispiel: True

#b) Eine Liste mit drei verschiedenen Datentypen könnte so aussehen: [42, 3.14, "Hallo Welt"]. Um den Typ jedes Elements zu bestimmen, verwendet man die type() Funktion wie folgt:

meine_liste = [42, 3.14, "Hallo Welt"]
print("Dieser Code gibt aus:")
for element in meine_liste:
    print(type(element))
    


#c) Um eine Ganzzahl in eine Gleitkommazahl umzuwandeln, verwendet man die float() Funktion. Beispiel:

ganzzahl = 42
gleitkommazahl = float(ganzzahl)
print("Die gleitkommazahl ist ", gleitkommazahl)  # Gibt 42.0 aus

#d) Ein Tupel ist eine Sammlung, die geordnet, aber unveränderlich ist. Im Gegensatz dazu ist eine Liste geordnet und veränderlich. Das bedeutet, dass man die Elemente einer Liste ändern kann, die eines Tupels jedoch nicht. Beispiel für ein Tupel: (42, 3.14, "Hallo Welt")

#e) Ein kurzes Python-Programm, das eine Zeichenkette und eine Ganzzahl nimmt, die Ganzzahl in eine Zeichenkette umwandelt und beide zusammenfügt:

# Eingabe
str1 = "Die Antwort ist "
num = input('Enter a number ')
#num = 42
# Verarbeitung
str2 = str(num)  # Umwandlung der Ganzzahl in eine Zeichenkette
result = str1 + str2  # Zusammenfügen der Zeichenketten
# Ausgabe
print(result)  # Gibt "Die Antwort ist 42" aus
