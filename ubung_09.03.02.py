# Entwickle ein Python-Skript, das folgende Aufgaben erfüllt:

import json
import re


# a) Lese eine Textdatei namens "tagebuch.txt", die in UTF-8 kodiert ist, 
# und speichere den Inhalt in einer Variablen. Verwende die with-answeisung und try-except-Blöcke, 
# um Fehler beim Dateizugriff zu handhaben.
try:
    with open('tagebuch.txt', mode='r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei 'tagebuch.txt' wurde nicht gefunden.")

# b) Verwende eine Funktion, um alle Vorkommen eines bestimmten Wortes im Text zu zählen. 
# Das Wort soll als Parameter an die Funktion übergeben werden.
def worter_zahlen(wort):
    gefunden = re.findall(wort, inhalt)
    return len(gefunden)

print(worter_zahlen('ein'))

# c) Ersetze in dem Text alle Vorkommen des Wortes "traurig" durch "glücklich" und speichere 
# das Ergebnis in einer neuen Datei namens "tagebuch_neu.txt".
def ersetze_text():
    neuer_text = inhalt.replace('traurig', 'glücklich')
    print(neuer_text)
    try:
        with open('tagebuch_neu.txt', 'w', encoding='utf-8') as stream:
                stream.write(neuer_text)
    except OSError as e:                       # проблемы с файлами/диском
        print(f"Fehler beim Speichern: {e}")
    except (TypeError, ValueError) as e:       # проблемы с данными
        print(f"Ungültige Daten: {e}")

ersetze_text()


# d) Schreibe eine weitere Funktion, die den aktualisierten Text nimmt und eine Liste von 
# Sätzen zurückgibt, wobei jeder Satz ein Element der Liste ist. Verwende dazu eine geeignete String-Methode.
def teile_in_saetze(text):
    return text.split('.')

# e) Konvertiere die Liste von Sätzen in ein JSON-Format und speichere diese Daten in 
# einer Datei namens "tagebuch_saetze.json".

# Stelle sicher, dass dein Skript modular aufgebaut ist und du Import-Module für 
# JSON-Funktionalitäten und andere benötigte Funktionen verwendest.

# import json
# def zaehle_wort(text, wort):
#     return text.lower().count(wort.lower())
# def ersetze_wort(text, alt, neu):
#     return text.replace(alt, neu)
# def teile_in_saetze(text):
#     return text.split('.')
# def speichere_als_json(dateiname, daten):
#     with open(dateiname, 'w', encoding='utf-8') as file:
#         json.dump(daten, file, ensure_ascii=False, indent=4)
# try:
#     with open('tagebuch.txt', 'r', encoding='utf-8') as file:
#         inhalt = file.read()
# except FileNotFoundError:
#     print("Die Datei wurde nicht gefunden.")
# else:
#     wort_vorkommen = zaehle_wort(inhalt, 'traurig')
#     print(f"Das Wort 'traurig' kommt {wort_vorkommen} Mal vor.")
    
#     aktualisierter_text = ersetze_wort(inhalt, 'traurig', 'glücklich')
    
#     with open('tagebuch_neu.txt', 'w', encoding='utf-8') as neue_datei:
#         neue_datei.write(aktualisierter_text)
    
#     saetze = teile_in_saetze(aktualisierter_text)
#     speichere_als_json('tagebuch_saetze.json', saetze)
