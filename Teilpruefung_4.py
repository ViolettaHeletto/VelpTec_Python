# Entwickle ein Python-Programm, das eine Textdatei mit Kundenfeedback aus verschiedenen 
# Ländern analysiert. Das Programm soll folgende Funktionen umfassen:

# a) Lese die Textdatei feedback.txt, die Kundenkommentare in verschiedenen 
# Sprachen enthält. Verwende die with-Anweisung und stelle sicher, 
# dass die Datei korrekt geschlossen wird, nachdem sie gelesen wurde.

# b) Verwende reguläre Ausdrücke, um alle Datumsangaben 
# im Format DD.MM.YYYY aus dem Text zu extrahieren und speichere diese in einer Liste.

# c) Zähle, wie oft jedes Datum vorkommt, und speichere die Ergebnisse in einem Dictionary, 
# wobei das Datum der Schlüssel und die Anzahl der Vorkommen der Wert ist.

# d) Identifiziere alle Kommentare, die das Wort "exzellent" in beliebiger Groß- 
# oder Kleinschreibung enthalten. Speichere diese Kommentare in einer separaten Liste.

# e) Nutze die json-Modul, um das Dictionary mit den Datumsvorkommen und 
# die Liste der "exzellenten" Kommentare in zwei separaten Dateien (datums_vorkommen.json und exzellente_feedbacks.json) 
# zu speichern.

# f) Implementiere eine Fehlerbehandlung mit try und except, um elegante Lösungen 
# für mögliche I/O-Fehler und Probleme beim Arbeiten mit Dateien zu bieten.

# g) Verwende Unicode-Nummern, um spezielle Zeichen oder Emojis in die Ausgabe einzufügen, 
# die den Erfolg der Operation signalisieren. 

# h) Erstelle eine Textdatei entsprechend den obigen Punkten um deinen Code zu testen.

import re
from pathlib import Path
import json

def lese_feedback(dateiname):
    """Liest die Feedback-Datei mit der with-Anweisung ein."""
    with open(dateiname, 'r', encoding='utf-8') as datei:
        return datei.read()

def datumsangaben_suchen(text):
    return re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)

def zahle_datum(datum_list):
    vorkommen = {}
    for date in datum_list:
        vorkommen[date] = vorkommen.get(date, 0) + 1
    return vorkommen

def finde_kommentare_mit_wort(text, wort):
    kommentare_mit_wort = []
    for zeile in text.splitlines():
        if re.search(wort, zeile, re.IGNORECASE):
            kommentar = zeile.strip()
            if kommentar:
                kommentare_mit_wort.append(kommentar)
    return kommentare_mit_wort

def speichere_json(daten, dateiname):
    """Speichert Daten als JSON-Datei."""
    with open(dateiname, 'w', encoding='utf-8') as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=4)


def main():
    eingabe_datei = Path(__file__).parent / 'Teilprufung_4' / 'feedback.txt'
    ausgabe_datum = 'datums_vorkommen.json'
    ausgabe_exzellent = 'exzellente_feedbacks.json'

    try:
        # a) Datei lesen
        inhalt = lese_feedback(eingabe_datei)
        print("\u2705 Datei erfolgreich gelesen:", eingabe_datei)

        # b) Datumsangaben extrahieren
        datum_liste = datumsangaben_suchen(inhalt)
        print(f"\U0001F4C5 Gefundene Datumsangaben: {len(datum_liste)}")

        # c) Datum zählen
        datum_vorkommen = zahle_datum(datum_liste)
        print("\U0001F4CA Datumsvorkommen:")
        for datum, anzahl in sorted(datum_vorkommen.items()):
            print(f"   {datum}: {anzahl}x")

        # d) Exzellente Kommentare identifizieren
        exzellente = finde_kommentare_mit_wort(inhalt, 'exzellent')
        print(f"\u2B50 Kommentare mit 'exzellent': {len(exzellente)}")
        for k in exzellente:
            print(f"   \u2794 {k}")

        # e) In JSON-Dateien speichern
        speichere_json(datum_vorkommen, ausgabe_datum)
        speichere_json(exzellente, ausgabe_exzellent)
        print(f"\U0001F4BE Gespeichert: {ausgabe_datum}")
        print(f"\U0001F4BE Gespeichert: {ausgabe_exzellent}")

        print("\U0001F389 Analyse erfolgreich abgeschlossen!")

    except FileNotFoundError:
        print(f"\u274C Fehler: Die Datei '{eingabe_datei}' wurde nicht gefunden.")
    except PermissionError:
        print("\u274C Fehler: Keine Berechtigung zum Lesen/Schreiben der Datei.")
    except UnicodeDecodeError:
        print("\u274C Fehler: Die Datei konnte nicht als UTF-8 gelesen werden.")
    except json.JSONDecodeError as e:
        print(f"\u274C Fehler beim Verarbeiten von JSON: {e}")
    except OSError as e:
        print(f"\u274C Allgemeiner I/O-Fehler: {e}")
    except Exception as e:
        print(f"\u274C Unerwarteter Fehler: {e}")


if __name__ == '__main__':
    main()