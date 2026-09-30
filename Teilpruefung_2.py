# Du arbeitest für ein Unternehmen, das eine Software zur Verwaltung von Büchereien entwickelt. 
# Deine Aufgabe ist es, ein Python-Programm zu schreiben, das folgende Funktionalitäten bietet:

# Datenbankstruktur:
# Liste von Wörterbüchern: Jedes Buch ist ein eigenes Wörterbuch
# mit den Schlüsseln "Titel", "Autor", "Jahr"
buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019},
    {"Titel": "Harry Potter", "Autor": "J.K.Rowling", "Jahr": 2001}
] 


# a) Buchsuche: Eine Funktion suche_buch(titel, autor=None), 
# die Bücher nach Titel und optional nach Autor sucht. 
# Die Funktion gibt eine Liste von Büchern zurück, die den Suchkriterien entsprechen. 
# Wenn kein Autor angegeben ist, werden alle Bücher mit dem entsprechenden Titel zurückgegeben.

def suche_buch(lst, titel, autor = None):
    gesuchte_buecher = []  # hier sammeln wir die gefundenen Bücher
    for el in lst:
        if el["Titel"] == titel and (autor is None or el["Autor"] == autor):
            gesuchte_buecher.append(el)
    zeige_datenbank(gesuchte_buecher)
    return gesuchte_buecher


# b) Buch hinzufügen: Eine Funktion fuege_buch_hinzu(titel, autor, jahr), 
# die ein neues Buch zur Bücherei-Datenbank hinzufügt. 
# Die Datenbank wird als Liste von Wörterbüchern dargestellt, wobei jedes Wörterbuch ein Buch repräsentiert.

def fuege_buch_hinzu(lst, titel, autor, jahr):
    buch_dict = {"Titel": titel, "Autor": autor, "Jahr": jahr}
    lst.append(buch_dict)

# c) Bücher nach Jahr filtern: Eine Funktion buecher_nach_jahr(jahr), 
# die alle Bücher zurückgibt, die in einem bestimmten Jahr veröffentlicht wurden. 
# Verwende die filter()-Funktion, um diese Aufgabe zu erfüllen.

def buecher_nach_jahr(lst, jahr):
    gesuchte_buecher_jahr = list(filter(lambda el: el["Jahr"] == jahr, lst))
    zeige_datenbank(gesuchte_buecher_jahr)
    return gesuchte_buecher_jahr

# d) Anzeige der Bücherei-Datenbank: Eine Funktion zeige_datenbank(), 
# die den aktuellen Inhalt der Bücherei-Datenbank in einer formatierten Ausgabe anzeigt. 
# Hierbei soll jeder Eintrag folgende Informationen enthalten: Titel, Autor, Erscheinungsjahr.

def zeige_datenbank(lst):
    for i, buch in enumerate(lst, start=1):
        print(f"{i}. {buch['Titel']} – {buch['Autor']} ({buch['Jahr']})")


# e) Interaktives Menü: Implementiere ein interaktives Menü, das es dem Benutzer ermöglicht, 
# die oben genannten Funktionen auszuführen. Verwende eine Schleife mit while, 
# um das Menü kontinuierlich anzuzeigen, bis der Benutzer sich entscheidet, das Programm zu beenden.


print('Willkommen in der Bibliothek!')
while True:
    aktion = input('Was möchten Sie sehen? (Suche Buch(SB), fuege Buch hinzu(F), suche nach Jahr(SJ), zeige Datenbank(D)) ').strip().upper()
    if aktion == 'SB':
        name_buch = input('Welche Buch möchten Sie sehen? ')
        author_buch = input('Kennen Sie den Autor? ').strip() or None
        suche_buch(buecherei_datenbank, name_buch, author_buch)
    elif aktion == 'F':
        name_buch_fuege = input('Welches Buch möchten Sie hinzufügen? ')
        author_buch_fuege = input('Autor des Buches: ')
        try:
            jahr_buch_fuege = int(input('Erscheinungsjahr: '))
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue
        fuege_buch_hinzu(buecherei_datenbank, name_buch_fuege, author_buch_fuege, jahr_buch_fuege)
    elif aktion == 'SJ':
        try:
            jahr_buch_suche = int(input('In welchem Jahr wurde das Buch veröffentlicht? '))
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue
        buecher_nach_jahr(buecherei_datenbank, jahr_buch_suche)
    elif aktion == 'D':
        zeige_datenbank(buecherei_datenbank)
    

    weiter = input("Möchten Sie die Bibliothek weiterhin nutzen? (ja/nein): ").lower()
    if weiter != "ja":
        print("Programm beendet.")
        break
