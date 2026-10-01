# Entwickle ein Python-Skript, das folgende Aufgaben ausführt und dabei die genannten Themenbereiche abdeckt. Du hast 90 Minuten Zeit, um diese Übung zu bearbeiten.

# a) Definiere eine Funktion speichere_daten, die als Parameter eine Liste von Tupeln entgegennimmt. Jedes Tupel enthält zwei Werte: einen Namen (String) und ein Alter (Integer). Die Funktion soll diese Daten in einer Datei namens personen.txt speichern. Verwende dabei die with-Anweisung und den Modus 'w' zum Öffnen der Datei. Jedes Tupel soll in einer neuen Zeile in folgendem Format gespeichert werden: Name: Alter.

# b) Definiere eine weitere Funktion lade_daten, die die zuvor gespeicherten Daten aus der Datei personen.txt liest und als Liste von Dictionaries zurückgibt, wobei jedes Dictionary einen Namen und ein Alter enthält.

# c) Implementiere eine Fehlerbehandlung in beiden Funktionen, um mit möglichen Laufzeitfehlern umzugehen, z.B. wenn die Datei nicht existiert oder ein Schreib-/Lesefehler auftritt. Gib in solchen Fällen eine aussagekräftige Fehlermeldung aus.

# d) Schreibe eine Kontrollstruktur, die überprüft, ob die zurückgegebene Liste von lade_daten leer ist oder nicht. Wenn sie nicht leer ist, gib die geladenen Daten formatiert in der Konsole aus. Verwende dazu eine Schleife. 

def speichere_daten(liste_von_tupeln):
    with open('namen.txt', 'w') as stream:
        for name, alter in liste_von_tupeln:
            stream.write(f"{name}: {alter}\n")

#AI 
# def speichere_daten(personen_liste):
#     try:
#         with open('personen.txt', 'w', encoding='utf-8') as datei:
#             for name, alter in personen_liste:
#                 datei.write(f"{name}: {alter}\n")
#     except OSError as e:                       # проблемы с файлами/диском
#         print(f"Fehler beim Speichern: {e}")
#     except (TypeError, ValueError) as e:       # проблемы с данными
#         print(f"Ungültige Daten: {e}")

def lade_daten(dateiname):
    daten = {}
    with open(dateiname, 'r', encoding='utf-8') as datei:
        for zeile in datei:
            zeile = zeile.strip()          # убираем \n и пробелы по краям
            if not zeile:                  # пропускаем пустые строки
                continue
            name, alter = zeile.split(': ')  # разбиваем по разделителю
            daten[name] = int(alter)       # возраст → число
    return daten

# try exept 
# def lade_daten(dateiname):
#     daten = {}
#     try:
#         with open(dateiname, 'r', encoding='utf-8') as datei:
#             for zeile_nr, zeile in enumerate(datei, 1):
#                 zeile = zeile.strip()
#                 if not zeile:
#                     continue
#                 try:
#                     name, alter = zeile.split(': ', 1)
#                     daten[name] = int(alter)
#                 except ValueError:
#                     print(f"Zeile {zeile_nr} übersprungen: {zeile!r}")
#     except FileNotFoundError:
#         print(f"Datei '{dateiname}' existiert nicht.")
#     except PermissionError:
#         print(f"Keine Berechtigung für '{dateiname}'.")
#     return daten

def main():
    tupel_name_alter = {('Alisa', 29), ('Violetta', 26), ('Ed', 28), ('Rita', 29)}
    speichere_daten(tupel_name_alter)
    geladene_daten = lade_daten('namen.txt')
    if geladene_daten:
        personen = lade_daten('namen.txt')
        print(personen)
    else:
        print("Keine Daten geladen.")
if __name__ == "__main__":
    main()
