# Erstelle ein Python-Skript, das folgende Aufgaben erfüllt:
import re
import json

# a) Definiere eine Variable text, die einen mehrzeiligen String speichert, 
# welcher Sonderzeichen und Unicode-Zeichen enthält. Verwende mindestens 
# drei verschiedene Escape-Sequenzen und zwei Unicode-Zeichen 
# (z.B. ein Emoji und ein Zeichen aus einem anderen Schriftsystem).
text = "Hier ist ein Beispieltext mit einigen besonderen Zeichen: \nNeue Zeile, \tTabulator, \\Backslash, \u2764Herz Emoji, \U0001F600Grinsendes Gesicht."

# b) Zähle, wie oft ein bestimmtes Wort in text vorkommt. 
# Das Wort soll als Eingabe über die Konsole gegeben werden.
def worter_zahlen(wort):
    gefunden = re.findall(wort, text)
    print(len(gefunden))

# c) Ersetze in text alle Vorkommen eines bestimmten Wortes 
# (ebenfalls über die Konsole eingegeben) durch ein anderes Wort 
# (auch über die Konsole eingegeben) und gib den neuen Text aus.
def ersetze(alte_wort, neu_wort):
    neu_text = text.replace(alte_wort, neu_wort)
    print(neu_text)
    return neu_text

# d) Speichere den modifizierten Text in einer Datei mit dem Namen modifizierter_text.txt 
# unter Verwendung der with-Anweisung.
def ersetze_text(neu_text):
    try:
        with open('modifizierter_text.txt', 'w', encoding='utf-8') as stream:
                stream.write(neu_text)
    except OSError as e:                       # проблемы с файлами/диском
        print(f"Fehler beim Speichern: {e}")
    except (TypeError, ValueError) as e:       # проблемы с данными
        print(f"Ungültige Daten: {e}")

# e) Dies eine Datei namens daten.json, die eine Liste von Dictionaries enthält, ein. 
# Verwende das JSON-Modul, um die Datei zu laden. Gib anschließend die Daten in der Konsole aus. 

try:
    with open('daten.json', 'r', encoding='utf-8') as datei:
        daten = json.load(datei)
        print("Inhalt der 'daten.json':")
        print(daten)
except FileNotFoundError:
    print("Die Datei 'daten.json' wurde nicht gefunden.")