# Erstelle ein Python-Skript, das folgende Aufgaben ausführt:

# a) Definiere eine Variable text, die einen mehrzeiligen String speichert. 
# Der String soll mindestens ein Unicode-Zeichen, eine Escape-Sequenz und variable 
# Teile enthalten, die durch die format() Methode ersetzt werden. 
# Verwende für das Unicode-Zeichen ein Emoji und für die Escape-Sequenz einen Zeilenumbruch.

# b) Verwende die print() Funktion, um den String auszugeben.

# c) Lese eine Textdatei namens beispiel.txt, die du zuvor selbst erstellen musst, 
# mit der with-Anweisung und utf-8 Encoding. Speichere den Inhalt der Datei in einer Variablen und gib ihn aus.

# d) Schreibe eine Funktion speichere_json, die ein Python-Objekt 
# (z.B. ein Dictionary mit einigen Schlüssel-Wert-Paaren) in eine Datei im JSON-Format speichert. 
# Verwende dazu das Modul json.

# e) Verwende die try und except Blöcke, um Fehler beim Lesen einer nicht existierenden 
# Datei zu behandeln. Gib eine benutzerfreundliche Nachricht aus, wenn die Datei nicht gefunden wird. 
import json

text = "Hier ist ein Beispieltext mit einem Emoji: \U0001F600 und einem Zeilenumbruch\nHier ist der zweite Teil des Textes, der {0} enthält."
print(text)

try:
    with open('studentendaten.txt', mode='r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei 'studentendaten.txt' wurde nicht gefunden.")

def speichere_json(data, dateiname):
    with open(dateiname, 'w', encoding='utf-8') as datei:
        json.dump(data, datei, ensure_ascii=False, indent=4)

speichere_json(inhalt, 'studentendaten.json')

try:
    with open('nicht_existierende_datei.txt', mode='r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei 'nicht_existierende_datei.txt' wurde nicht gefunden.")
