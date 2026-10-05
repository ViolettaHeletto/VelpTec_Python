# Du arbeitest als Entwickler in einem Unternehmen, das eine Software zur Verwaltung von Kundenkontakten entwickelt. Deine Aufgabe ist es, ein Python-Modul zu erstellen, das folgende Funktionalitäten umfasst:

# a) Erstelle eine Funktion speichere_kontakt, die als Parameter die Daten eines Kontakts (Name, E-Mail, Telefonnummer) entgegennimmt und diese in einer JSON-Datei speichert. Verwende dabei das JSON-Format. Achte darauf, dass bei jedem Aufruf der Funktion ein neuer Kontakt zur Datei hinzugefügt wird, ohne die bestehenden Daten zu überschreiben.

# b) Implementiere eine Funktion lade_kontakte, die die gespeicherten Kontaktdaten aus der JSON-Datei liest und als Liste von Dictionaries zurückgibt. Jedes Dictionary in der Liste soll die Daten eines Kontakts repräsentieren.

# c) Erstelle eine Fehlerbehandlung für beide Funktionen, um sicherzustellen, dass das Programm nicht abstürzt, falls die Datei nicht existiert oder beschädigt ist. Gib in solchen Fällen eine entsprechende Fehlermeldung aus.

# d) Schreibe eine einfache Benutzeroberfläche (CLI), über die ein Benutzer neue Kontakte hinzufügen und die gespeicherten Kontakte anzeigen lassen kann. Verwende dazu die Funktionen speichere_kontakt und lade_kontakte.

import json
DATEINAME = "kontakten.json"

def speichere_kontakt(name, email, telefon):
    # 1. Читаем то, что уже есть
    try:
        with open(DATEINAME) as stream:
            messungen = json.load(stream)
    except (FileNotFoundError, json.JSONDecodeError):
        messungen = []

    # 2. Добавляем новые данные в список
    messungen.append([name, email, telefon])

    # 3. Один раз записываем итог обратно
    with open(DATEINAME, 'w') as stream:
        json.dump(messungen, stream)

def lade_kontakte():
    """
    Liest alle Kontakte aus der JSON-Datei und gibt sie als Liste von
    Dictionaries zurück.
    """
    # b) + c) Lesen mit Fehlerbehandlung
    try:
        with open(DATEINAME, 'r', encoding='utf-8') as stream:
            kontakte = json.load(stream)
    except FileNotFoundError:
        print(f"Hinweis: Datei '{DATEINAME}' existiert nicht.")
        return []
    except json.JSONDecodeError:
        print(f"Fehler: Datei '{DATEINAME}' ist beschädigt und kann nicht gelesen werden.")
        return []
    except OSError as e:
        print(f"Fehler beim Lesen der Datei: {e}")
        return []

    # Sicherstellen, dass es eine Liste ist
    if not isinstance(kontakte, list):
        print("Warnung: Dateiinhalt ist kein Array. Gebe leere Liste zurück.")
        return []

    return kontakte


# Добавление в конец файла, без предыдущего сохранения в объект. JSON Lines
def write_in_ende_append(name, email, telefon):
    kontakten = [name, email, telefon]
    with open(DATEINAME, 'a') as stream:
        json.dump(kontakten, stream)
        stream.write('\n')

# speichere_kontakt('ekjfr', 'grr5th', '11111111')
# speichere_kontakt('35ekjfr', '34dfsgrr5th', '222222222')
# speichere_kontakt('w345ekjfr', 'wew3grr5th', '33333333')
# speichere_kontakt('35etekjfr', 'grr5erf3th', '4444444')
# speichere_kontakt('ekjet4ytfr', 'grr5tefegfh', '5555555')



write_in_ende_append('aaaaaa', 'bbbbbb', '776666')
write_in_ende_append('aaaaaa', 'bbbbbb', '776666')
write_in_ende_append('aaaaaa', 'bbbbbb', '888')
write_in_ende_append('aaaaaa', 'bbbbbb', '9999')


def benutzeroberflaeche():
    while True:
        aktion = input("Möchten Sie einen neuen Kontakt speichern (s) oder vorhandene Kontakte anzeigen (a)? (s/a/beenden): ")
        if aktion.lower() == 'beenden':
            break
        elif aktion.lower() == 's':
            name = input("Name: ")
            email = input("E-Mail: ")
            telefon = input("Telefonnummer: ")
            speichere_kontakt(name, email, telefon)
            print("Kontakt gespeichert.")
        elif aktion.lower() == 'a':
            kontakte = lade_kontakte()
            if kontakte:
                for kontakt in kontakte:
                    print(f"Name: {kontakt['Name']}, E-Mail: {kontakt['E-Mail']}, Telefonnummer: {kontakt['Telefonnummer']}")
            else:
                print("Keine Kontakte gefunden.")
        else:
            print("Ungültige Eingabe.")
if __name__ == "__main__":
    benutzeroberflaeche()