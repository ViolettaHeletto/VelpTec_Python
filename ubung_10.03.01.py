# Du sollst ein Python-Skript schreiben, das folgende Funktionen ausführt:
import os

# a) Erstelle eine Funktion erstelle_verzeichnis, die als Argument einen Verzeichnisnamen (String) nimmt. 
# Die Funktion soll mithilfe des os-Moduls überprüfen, ob das Verzeichnis bereits existiert. Falls nicht, 
# soll das Verzeichnis erstellt werden. Gib eine Bestätigung aus, dass das Verzeichnis erstellt wurde oder bereits existiert.
def erstelle_verzeichnis(verzeichnisnamen):
    if os.path.exists(verzeichnisnamen) and os.path.isdir(verzeichnisnamen):
        print("das Verzeichnis bereits existiert")
    else:
        os.mkdir(verzeichnisnamen)
        print(f"Das Verzeichnis '{verzeichnisnamen}' wurde erfolgreich erstellt.")

# Вот правильный "защищенный" вариант:

# python
# import os

# def erstelle_verzeichnis(verzeichnisnamen):
#     if os.path.exists(verzeichnisnamen):
#         # Проверяем: это папка или файл?
#         if os.path.isdir(verzeichnisnamen):
#             print(f"Das Verzeichnis '{verzeichnisnamen}' existiert bereits.")
#         else:
#             # По этому пути лежит ФАЙЛ, а не папка
#             print(f"FEHLER: '{verzeichnisnamen}' ist eine Datei, kein Verzeichnis!")
#     else:
#         os.makedirs(verzeichnisnamen, exist_ok=True)
#         print(f"Das Verzeichnis '{verzeichnisnamen}' wurde erstellt.")

# b) Erstelle eine Funktion speichere_text_in_datei, die zwei Argumente nimmt: den Dateinamen (String) 
# und den zu speichernden Text (String). Die Funktion soll den Text in der angegebenen Datei speichern. 
# Verwende die with-Anweisung, um die Datei zu öffnen und sicherzustellen, dass sie korrekt geschlossen wird.

def speichere_text_in_datei(dateiname, text):
    with open(dateiname, 'w') as datei:
        datei.write(text)
    print(f"Text wurde in '{dateiname}' gespeichert.")


# c) Erstelle eine Funktion lese_datei, die als Argument einen Dateinamen (String) nimmt und 
# den Inhalt der Datei ausgibt. Fange mögliche Ausnahmen ab, die beim Versuch, die Datei zu lesen, 
# auftreten können (z.B. wenn die Datei nicht existiert), und gib eine entsprechende Fehlermeldung aus.
def lese_datei(dateiname):
    try:
        with open(dateiname, 'r') as datei:
            inhalt = datei.read()
            print(f"Inhalt von '{dateiname}':\n{inhalt}")
    except FileNotFoundError:
        print(f"Die Datei '{dateiname}' wurde nicht gefunden.")


# d) Erstelle eine Funktion liste_dateien_in_verzeichnis, die als Argument einen Verzeichnisnamen 
# (String) nimmt und alle Dateien in diesem Verzeichnis auflistet. Verwende das os-Modul, um auf das Dateisystem zuzugreifen.
def liste_dateien_in_verzeichnis(verzeichnisname):
    dateien = os.listdir(verzeichnisname)
    print(f"Dateien in '{verzeichnisname}':")
    for datei in dateien:
        print(datei)


# e) Schreibe ein Hauptprogramm, das die Funktionen in folgender Reihenfolge aufruft: erstelle_verzeichnis 
# mit dem Verzeichnisnamen "MeineDaten", speichere_text_in_datei mit einem beliebigen Text in einer 
# Datei namens "beispiel.txt" im Verzeichnis "MeineDaten", 
# lese_datei für "beispiel.txt" und liste_dateien_in_verzeichnis für das Verzeichnis "MeineDaten". 

verzeichnisname = "MeineDaten"
dateiname = os.path.join(verzeichnisname, "beispiel.txt")
text = "Das ist ein Beispieltext."


erstelle_verzeichnis(verzeichnisname)
speichere_text_in_datei(dateiname, text)
lese_datei(dateiname)
liste_dateien_in_verzeichnis(verzeichnisname)