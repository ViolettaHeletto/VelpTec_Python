# Entwickle ein Python-Skript, das folgende Funktionen implementiert:

# a) Erstelle eine Funktion erstelle_datei, die eine neue Textdatei mit einem vorgegebenen Namen 
# und Inhalt in einem spezifischen Verzeichnis erstellt. Verwende dazu die with-Anweisung 
# und stelle sicher, dass Fehler, wie z.B. fehlende Schreibberechtigungen, 
# mit try und except abgefangen werden.

import os

def erstelle_datei(dateiname, inhalt, verzeichnis='.'):
    voller_pfad = os.path.join(verzeichnis, dateiname)
    try:
        with open(voller_pfad, 'w') as datei:
            datei.write(inhalt)
        print(f"Datei '{dateiname}' wurde erfolgreich erstellt.")
    except Exception as e:
        print(f"Fehler beim Erstellen der Datei '{dateiname}': {e}")

# b) Implementiere eine Funktion listdir_filter, die alle Dateien eines Verzeichnisses auflistet, 
# die eine bestimmte Dateiendung haben (z.B. .txt). Nutze dazu das Modul os und eine List Comprehension.
def listdir_filter(verzeichnis, endung):
    return [datei for datei in os.listdir(verzeichnis) if datei.endswith(endung)]

# c) Schreibe eine Funktion umbenennen_dateien, die alle Dateien eines Verzeichnisses, 
# die eine bestimmte Endung haben, umbenennt, indem sie ein Präfix hinzufügt. 
# Verwende dazu das Modul os.

def umbenennen_dateien(verzeichnis, alte_endung, präfix):
    for datei in os.listdir(verzeichnis):
        if datei.endswith(alte_endung):
            neuer_name = präfix + datei
            os.rename(os.path.join(verzeichnis, datei), os.path.join(verzeichnis, neuer_name))
    print(f"Dateien wurden umbenannt.")

# d) Entwickle eine Funktion json_speichern, die eine Liste von Dictionaries 
# in eine Datei im JSON-Format speichert. Verwende dazu das Modul json.
import json
def json_speichern(daten, dateiname):
    with open(dateiname, 'w') as datei:
        json.dump(daten, datei)

# e) Implementiere eine Funktion json_laden, die eine JSON-Datei liest und 
# den Inhalt als Python-Objekt zurückgibt.
def json_laden(dateiname):
    with open(dateiname, 'r') as datei:
        return json.load(datei)

# f) Erstelle eine Funktion regex_suche, die in allen .txt-Dateien eines Verzeichnisses 
# nach einem regulären Ausdruck sucht und die Namen der Dateien zurückgibt, in denen die Suche erfolgreich war.
import re
def regex_suche(verzeichnis, regex):
    passende_dateien = []
    for datei in os.listdir(verzeichnis):
        if datei.endswith('.txt'):
            with open(os.path.join(verzeichnis, datei), 'r') as f:
                inhalt = f.read()
                if re.search(regex, inhalt):
                    passende_dateien.append(datei)
    return passende_dateien

# Für jede dieser Funktionen sollst du ein kurzes Beispiel für deren Aufruf und Verwendung schreiben.

erstelle_datei('test.txt', 'Das ist ein Test.', 'MeineDaten')
print(listdir_filter('.', '.txt'))
meine_daten = [{'name': 'Anna', 'alter': 28}, {'name': 'Bernd', 'alter': 35}]
json_speichern(meine_daten, 'daten.json')
geladene_daten = json_laden('daten.json')
print(geladene_daten)
print(regex_suche('.', r'\bTest\b'))
