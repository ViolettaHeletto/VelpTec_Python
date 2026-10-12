# Erstelle ein Python-Programm, das folgende Aufgaben erfüllt:

# a) Definiere eine Variable, die einen Text in Form eines Strings speichert. 
# Dieser Text soll mindestens ein Unicode-Zeichen enthalten,
#  welches nicht auf einer normalen Tastatur zu finden ist.
#  Verwende dazu die Funktion chr() mit einer Unicode-Nummer deiner Wahl.
text = "Das ist ein Beispieltext mit einem Unicode-Zeichen: " + chr(8364) # Euro-Zeichen

# b) Füge dem Text eine Escape-Sequenz hinzu, die einen Zeilenumbruch darstellt.
text += "\nDies ist eine neue Zeile."

# c) Verwende eine Stringmethode, um zu zählen, wie oft ein bestimmtes Zeichen in deinem Text vorkommt.
anzahl_e = text.count('e')
print(f"Das Zeichen 'e' kommt {anzahl_e} Mal im Text vor.")

# d) Erstelle eine Liste mit mehreren Strings. Verwende die Methode .join(), 
# um einen neuen String zu erstellen, der die Elemente der Liste durch ein Komma getrennt enthält.
string_liste = ['Python', 'ist', 'toll']
verbundener_string = ', '.join(string_liste)
print(verbundener_string)

# e) Speichere den Text aus a) in einer Datei. Verwende dazu die with-Anweisung und 
# den Modus 'w' für das Schreiben in Dateien.
with open('beispieltext.txt', 'w', encoding='utf-8') as datei:
    datei.write(text)

# f) Lies den Text aus der Datei, die du in e) erstellt hast, und gib ihn auf 
# der Konsole aus. Verwende dazu ebenfalls die with-Anweisung, diesmal mit dem Modus 'r' für das Lesen aus Dateien.
try:
    with open('beispieltext.txt', 'r', encoding='utf-8') as datei:
        gelesener_text = datei.read()
        print(gelesener_text)
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")

# g) Fange mögliche Ausnahmen, die beim Lesen der Datei auftreten können, 
# mit try und except ab.

# h) Verwende das JSON-Format, um eine einfache Datenstruktur 
# (z.B. ein Dictionary mit einigen Schlüssel-Wert-Paaren) in einer Datei zu speichern und wieder zu laden. 

import json
daten = {'name': 'Max', 'alter': 30}
with open('daten.json', 'w', encoding='utf-8') as datei:
    json.dump(daten, datei)
try:
    with open('daten.json', 'r', encoding='utf-8') as datei:
        geladene_daten = json.load(datei)
        print(geladene_daten)
except FileNotFoundError:
    print("Die JSON-Datei wurde nicht gefunden.")

