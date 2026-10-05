# Schreibe ein Python-Skript, das folgende Aufgaben erfüllt:

# a) Erstelle eine Liste mit den Namen von fünf Freunden.

# b) Speichere diese Liste in einer Datei mit dem Namen "freunde.txt" unter Verwendung des JSON-Formats.

# c) Lies die Liste aus der Datei "freunde.txt" und weise sie einer neuen Variablen zu.

# d) Füge der Liste in der Datei einen weiteren Namen hinzu, ohne die ursprüngliche Liste im Skript zu ändern.

# e) Fang mögliche Laufzeitfehler beim Öffnen, Schreiben und Lesen der Datei ab und gib eine benutzerfreundliche Fehlermeldung aus.

# f) Stelle sicher, dass die Datei in jedem Fall korrekt geschlossen wird, auch wenn Fehler auftreten. 

import json
#a) Liste mit Namen erstellen

freunde_liste = ["Anna", "Bernd", "Carla", "David", "Eva"]
#b) Liste in einer Datei speichern

try:
    with open("freunde.txt", "w") as file:
        json.dump(freunde_liste, file)
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Speichern der Liste: {e}")
#c) Liste aus der Datei lesen

try:
    with open("freunde.txt", "r") as file:
        geladene_liste = json.load(file)
        print("Geladene Freunde Liste:", geladene_liste)
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Laden der Liste: {e}")
#d) Einen weiteren Namen hinzufügen

try:
    with open("freunde.txt", "r+") as file:
        freunde = json.load(file)
        freunde.append("Felix")  # Neuen Namen hinzufügen
        file.seek(0)  # Zurück zum Anfang der Datei gehen
        json.dump(freunde, file)
        file.truncate()  # Entfernt überschüssige Daten am Ende der Datei
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Aktualisieren der Liste: {e}")


#e) und f) sind in den try-except-Blöcken und der with-Anweisung behandelt.