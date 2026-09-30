#a) Erstelle eine Liste von Tupeln, 
# wobei jedes Tupel aus einem Buchstaben und einer Zahl besteht. 
# Die Liste soll mindestens 5 Elemente enthalten.

variable_list = [(4, 'a'), (7, 'd'), (2.5, 'b'), (5, 'e'), (3, 't')]
#print(variable_list)

#b) Schreibe eine Funktion, die prüft, ob ein bestimmtes Element (Tupel aus Buchstabe und Zahl) 
# in der Liste vorhanden ist. Gib eine entsprechende Nachricht
# aus, z.B. "Element gefunden: (Buchstabe, Zahl)" oder "Element nicht gefunden".
elemente = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]
print(elemente)

def pruefe_element(buchstabe, zahl):
    if (buchstabe, zahl) in elemente:
        print(f"Element gefunden: ({buchstabe}, {zahl})")
    else:
        print("Element nicht gefunden.")
        
userBuch = 'B' #input('Enter symbol Buch: ')
useryahl = 2 #float(input('Enter symbol Zahl: '))
pruefe_element(userBuch, useryahl)

#c) Erstelle eine Funktion, die eine gegebene Zeichenkette in eine ganze Zahl umwandelt (Typecasting). 

def str_to_int(user_str):
    ready_int = int(user_str)
    return ready_int

input_str = input('Enter number: ')
number = str_to_int(input_str)
print(f"Your number is {number}, and type is {type(number)}")


#d) Kommentiere dein Skript ausführlich, 
# um die Logik hinter deinem Code zu erklären.

#e) Implementiere eine einfache Benutzerschnittstelle in der Konsole, 
# die es dem Benutzer ermöglicht, die Funktionen zu testen. Die Benutzerschnittstelle 
# sollte mindestens die Möglichkeit bieten, nach einem Element in der Liste zu suchen und eine 
# Zeichenkette in eine Zahl umzuwandeln.



#f) Füge eine Kontrollstruktur hinzu, die prüft, 
# ob die umgewandelte Zahl positiv, negativ oder Null ist, 
# und gib eine entsprechende Nachricht aus. 

while True:
    aktion = input("Wähle eine Aktion: 'suchen', 'umwandeln' oder 'beenden': ")
    if aktion == 'suchen':
        buchstabe = input("Gib den Buchstaben des Elements ein: ")
        zahl = int(input("Gib die Zahl des Elements ein: "))
        pruefe_element(buchstabe, zahl)
    elif aktion == 'umwandeln':
        zeichenkette = input("Gib eine Zeichenkette ein, die in eine Zahl umgewandelt werden soll: ")
        umgewandelte_zahl = str_to_int(zeichenkette)
        # f) Kontrollstruktur für umgewandelte Zahl
        if umgewandelte_zahl is not None:
            if umgewandelte_zahl > 0:
                print("Die Zahl ist positiv.")
            elif umgewandelte_zahl < 0:
                print("Die Zahl ist negativ.")
            else:
                print("Die Zahl ist Null.")
    elif aktion == 'beenden':
        break
    else:
        print("Ungültige Eingabe. Bitte versuche es erneut.")