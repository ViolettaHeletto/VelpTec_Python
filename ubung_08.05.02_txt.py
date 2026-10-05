# Erstelle ein Python-Programm, das folgende Funktionen umsetzt:

# a) Definiere eine Funktion speichere_daten, die als Parameter eine Liste von Tupeln entgegennimmt. Jedes Tupel soll Daten eines Studenten repräsentieren, bestehend aus (Name, Matrikelnummer, Studiengang). Die Funktion soll diese Daten in einer Textdatei namens studentendaten.txt speichern. Verwende die with-Anweisung, um sicherzustellen, dass die Datei korrekt geöffnet und geschlossen wird. Jeder Student soll in einer neuen Zeile in folgendem Format gespeichert werden: "Name: [Name], Matrikelnummer: [Matrikelnummer], Studiengang: [Studiengang]".

# b) Definiere eine zweite Funktion lade_daten, die die gespeicherten Daten aus der Datei studentendaten.txt liest und als Liste von Dictionaries zurückgibt, wobei jedes Dictionary die Daten eines Studenten enthält.

# c) Implementiere eine einfache Fehlerbehandlung in beiden Funktionen, um den Fall zu behandeln, dass die Datei nicht geöffnet oder gefunden werden kann. Gib in diesem Fall eine entsprechende Fehlermeldung aus. 

def speichere_daten(tupel_studenten):
    try:
        with open('studentendaten.txt', 'w') as stream:
            for student in tupel_studenten:
                zeile = f'Name: {student[0]}, Matrikelnummer: {student[1]}, Studiengang: {student[2]}\n'
                stream.write(zeile)
    except OSError as e:                       # проблемы с файлами/диском
        print(f"Fehler beim Speichern: {e}")
    except (TypeError, ValueError) as e:       # проблемы с данными
        print(f"Ungültige Daten: {e}")



def lade_daten():
    try:
        studenten = []
        with open('studentendaten.txt', 'r') as datei:
            for zeile in datei:
                name, matrikelnummer, studiengang = zeile.strip().split(", ")
                student = {
                    "Name": name.split(": ")[1],
                    "Matrikelnummer": matrikelnummer.split(": ")[1],
                    "Studiengang": studiengang.split(": ")[1]
                }
                studenten.append(student)
        return studenten
    except IOError:
        print("Fehler beim Laden der Datei.")
        return []


# Beispiel für die Verwendung der Funktionen

studenten_daten = [
    ("Max Mustermann", "123456", "Informatik"),
    ("Erika Musterfrau", "654321", "Wirtschaftsinformatik")
]


speichere_daten(studenten_daten)
geladene_daten = lade_daten()
print(geladene_daten)