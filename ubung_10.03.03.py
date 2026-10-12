# Erstelle ein Python-Skript, das folgende Aufgaben erfüllt:
import os
import json

# a) Verwende das Modul os und json, um ein Verzeichnis namens meine_daten zu erstellen, 
# falls es noch nicht existiert. Speichere in diesem Verzeichnis eine Datei namens daten.json, 
# die eine Liste von Wörterbüchern (Dictionaries) enthält. Jedes Wörterbuch soll die Schlüssel name, 
# alter und beruf mit entsprechenden Werten für drei fiktive Personen enthalten.
verzeichnis = 'meine_daten'
if not os.path.exists(verzeichnis):
    os.makedirs(verzeichnis)
daten = [
    {'name': 'Max Mustermann', 'alter': 30, 'beruf': 'Ingenieur'},
    {'name': 'Erika Musterfrau', 'alter': 25, 'beruf': 'Architektin'},
    {'name': 'John Doe', 'alter': 40, 'beruf': 'Lehrer'}
]
with open(os.path.join(verzeichnis, 'daten.json'), 'w') as datei:
    json.dump(daten, datei)

# b) Lese die Datei daten.json aus dem Verzeichnis meine_daten und gib die Inhalte auf der Konsole 
# aus. Verwende dazu die with-Anweisung und behandele mögliche Ausnahmen mit try und except.
try:
    with open(os.path.join(verzeichnis, 'daten.json'), 'r') as datei:
        gelesene_daten = json.load(datei)
        print(gelesene_daten)
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")


# c) Erweitere das Skript um eine Funktion aktualisiere_daten, die einen neuen Eintrag zu 
# der Liste in daten.json hinzufügt. Der neue Eintrag soll durch Benutzereingabe über die Konsole gesammelt werden. 
# Nutze dafür die Funktion input() für die Schlüssel name, alter, und beruf. 
# Speichere die aktualisierten Daten wieder in daten.json. 
def aktualisiere_daten():
    name = input("Name: ")
    alter = input("Alter: ")
    beruf = input("Beruf: ")
    neuer_eintrag = {'name': name, 'alter': alter, 'beruf': beruf}
    try:

        with open(os.path.join(verzeichnis, 'daten.json'), 'r+') as datei:
            daten = json.load(datei)
            daten.append(neuer_eintrag)
            datei.seek(0)
            json.dump(daten, datei)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
aktualisiere_daten()
