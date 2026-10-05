# a) Definiere eine Liste mit Namen einkaufsliste und fülle sie mit mindestens fünf verschiedenen Lebensmitteln (als Strings).

# e) Fange mögliche Laufzeitfehler ab, die beim Öffnen, Schreiben oder 
# Schließen der Datei auftreten können, indem du try und except Blöcke verwendest.

# f) Lies die einkaufsliste.txt Datei und gib ihren Inhalt Zeile für Zeile in der 
# Konsole aus. Verwende dabei ebenfalls die with-Anweisung und den read-Modus.

einkaufsliste = ['Apfel', 'Fleisch', 'Wasser', 'Brot', 'Kartoffel']


# b) Schreibe eine Funktion einkauf_hinzufuegen, die ein neues Lebensmittel zur einkaufsliste hinzufügt. 
# Die Funktion soll überprüfen, ob das Lebensmittel bereits in der Liste vorhanden ist. 
# Ist dies der Fall, soll eine entsprechende Nachricht ausgegeben werden 
# ("Lebensmittel bereits in der Liste!"), andernfalls soll das Lebensmittel hinzugefügt werden.

def einkauf_hinzufuegen(item):
    if item in einkaufsliste:
        print("Lebensmittel bereits in der Liste!")
    else:
        einkaufsliste.append(item)
        print("Lebensmittel hinzufugt.")

# d) Speichere die endgültige einkaufsliste in einer Datei namens einkaufsliste.txt 
# mithilfe der with-Anweisung und dem write-Modus. Achte darauf, jedes Lebensmittel 
# in einer neuen Zeile zu speichern.

def einkaufliste_speichern(lst):
    try:
        with open('einkaufsliste.txt', 'w') as stream:
            for el in lst:
                stream.write(str(el)+ '\n')

    except OSError as e:                       # проблемы с файлами/диском
        print(f"Fehler beim Speichern: {e}")
    except (TypeError, ValueError) as e:       # проблемы с данными
        print(f"Ungültige Daten: {e}")

def lesen_einkaufliste():
    try:
        with open('einkaufsliste.txt', 'r') as datei:
            inhalt = datei.readlines()
            print("Einkaufsliste:")
            for lebensmittel in inhalt:
                print(lebensmittel.strip())
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten beim Lesen der Datei: {e}")


# c) Nutze eine Schleife, um den Benutzer bis zu drei Mal nach neuen Lebensmitteln zu fragen, 
# die zur Liste hinzugefügt werden sollen. Verwende die Funktion einkauf_hinzufuegen für jeden Eingabewert.
def main():
    while True:
        aktion = input("Möchten Sie einen neuen Lebensmittel hinzufuegen (h)? Ist die Liste der Produkte endgültig(s)? (h/s/b fur beenden): ")
        if aktion.lower() == 'b':
            break
        elif aktion.lower() == 'h':
            lebensmittel = input("Lebensmittel: ")
            einkauf_hinzufuegen(lebensmittel)
        elif aktion.lower() == 's':
            einkaufliste_speichern(einkaufsliste)
        else:
            print("Ungültige Eingabe.")
if __name__ == "__main__":
    main()