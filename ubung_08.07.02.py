# a) Definiere eine Variable alter und weise ihr dein Alter als Ganzzahl zu.

# b) Definiere eine Liste hobbies mit mindestens drei deiner Hobbies als Strings.

# c) Definiere ein Tupel lieblingsfarben mit mindestens drei deiner Lieblingsfarben als Strings.

# d) Schreibe eine Schleife, die für jedes Hobby in hobbies ausgibt: 
# "Eines meiner Hobbies ist: [Hobby]."

# e) Definiere eine Funktion jahre_bis_rente, die das Alter als Parameter annimmt 
# und berechnet, wie viele Jahre du bis zur Rente (angenommen mit 65 Jahren) hast.
#  Die Funktion soll das Ergebnis zurückgeben.

# f) Importiere das Modul json und speichere die Daten aus hobbies und 
# lieblingsfarben in einem Dictionary mit den Schlüsseln "Hobbies" und 
# "Lieblingsfarben" in einer JSON-Datei namens persoenliche_daten.json.

# g) Verwende eine try-except-Block, um die Datei zu öffnen und sicherzustellen, 
# dass eine Nachricht "Fehler beim Speichern der Daten" ausgegeben wird, falls ein Fehler auftritt.

# h) Verwende die with-Anweisung, um sicherzustellen, dass die Datei korrekt 
# geschlossen wird, nachdem der Schreibvorgang abgeschlossen oder ein Fehler aufgetreten ist. 

import json

alter = 26

hobbies = ["Lesen", "Programmieren", "Wandern"]
lieblingsfarben = ("Blau", "Grün", "Rot")

for hobby in hobbies:

    print(f"Eines meiner Hobbies ist: {hobby}.")

def jahre_bis_rente(alter):
    return 65 - alter

daten = {
    "Hobbies": hobbies,
    "Lieblingsfarben": lieblingsfarben
}

try:
    with open('persoenliche_daten.json', 'w', encoding='utf-8') as file:
        json.dump(daten, file, ensure_ascii=False, indent=4)
except Exception as e:
    print("Fehler beim Speichern der Daten:", e)