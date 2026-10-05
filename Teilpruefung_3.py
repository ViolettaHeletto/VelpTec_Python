# a) Erstelle eine Funktion, die eine Liste von Namen aus einer Textdatei liest. 
# Die Datei soll dabei so strukturiert sein, dass jeder Name in einer neuen Zeile steht. 
# Verwende die with-Anweisung und try-except-Blöcke, um Fehler beim Lesen der Datei zu handhaben. 

# b) Erweitere das Programm um eine Funktion, die die gelesenen 
# Namen in ein JSON-Format umwandelt und in einer neuen Datei speichert. 
# Stelle sicher, dass die Datei korrekt geschlossen wird, auch wenn beim Schreiben ein Fehler auftritt. 

# c) Implementiere eine Benutzeroberfläche in der Konsole, die dem Benutzer erlaubt, 
# zwischen den Funktionen zu wählen und entsprechende Eingaben zu machen.

import json


def textdatei_to_list(textdatei):
    lst = []
    try:
        with open(textdatei, 'r') as stream:
            for name in stream:
                lst.append(name.strip())
    except FileNotFoundError:
        print(f"Datei '{textdatei}' existiert nicht.")
    except PermissionError:
        print(f"Keine Berechtigung für '{textdatei}'.")
    return lst

def list_to_json(lst):
    try:
        with open('namen_TP_3.json', 'w', encoding='utf-8') as stream:
                json.dump(lst, stream, ensure_ascii=False, indent=4)
    except PermissionError:
        print("Fehler: Kein Zugriff auf die Datei.")
    except OSError as e:
        print(f"Fehler beim Schreiben der Datei: {e}")



def benutzeroberfläche():
    datenlist = []
    while True:
        aktion = input("Möchten Sie Daten aus einer Datei in eine Liste (d) oder aus einer Liste in eine JSON-Datei übertragen(j)? (d/j/b fur beenden): ")
        if aktion.lower() == 'b':
            break
        elif aktion.lower() == 'd':
            datenlist = textdatei_to_list('namen_TP_3.txt')
            print(f'Ihre Daten: {datenlist}')
        elif aktion.lower() == 'j':
            list_to_json(datenlist)
        else:
            print("Ungültige Eingabe.")
if __name__ == "__main__":
    benutzeroberfläche()