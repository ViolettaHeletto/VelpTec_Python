# a) Eine Funktion buch_daten_speichern, die als Parameter den Titel eines Buches (String), 
# den Namen des Autors (String), das Veröffentlichungsjahr (Integer), 
# und optional die Anzahl der Seiten (Integer, Defaultwert 0) erhält. 
# Die Funktion soll alle diese Daten in einem Dictionary speichern, 
# wobei die Schlüssel titel, autor, jahr, und seiten sind. 
# Die Funktion gibt dieses Dictionary zurück.

# b) Eine Funktion buecher_sammlung, die eine Liste von Bücher-Dictionaries 
# (erstellt von buch_daten_speichern) als Parameter erhält und die Gesamtanzahl 
# der Seiten aller Bücher in der Liste berechnet. 
# Die Funktion gibt die Gesamtseitenzahl zurück.

# c) Verwende eine Schleife, um den Benutzer zur Eingabe von Daten für drei verschiedene Bücher aufzufordern. 
# Nutze dabei die Funktion buch_daten_speichern für jedes Buch und speichere jedes resultierende Dictionary in einer Liste.

# d) Nachdem alle Bücher eingegeben wurden, rufe die Funktion buecher_sammlung 
# mit der Liste der Bücher-Dictionaries als Argument auf, 
# um die Gesamtanzahl der Seiten aller Bücher zu berechnen.

# e) Gib die Gesamtanzahl der Seiten aller Bücher aus. 

def buch_daten_speichern(titel, autor, jahr, seiten=0):
    buch_dict = {"titel": titel, "autor": autor, "jahr": jahr, "seiten": seiten}
    return buch_dict

def buecher_sammlung(buecher_liste):
    gesamt_seiten = sum(buch["seiten"] for buch in buecher_liste)
    return gesamt_seiten

buecher_liste = []
for _ in range(3):
    titel = input("Gib den Titel des Buches ein: ")
    autor = input("Gib den Autor des Buches ein: ")
    jahr = int(input("Gib das Veröffentlichungsjahr des Buches ein: "))
    seiten = input("Gib die Anzahl der Seiten des Buches ein (optional): ")
    seiten = int(seiten) if seiten else 0
    buch_dict = buch_daten_speichern(titel, autor, jahr, seiten)
    buecher_liste.append(buch_dict)
gesamt_seiten = buecher_sammlung(buecher_liste)
print(f"Die Gesamtanzahl der Seiten aller Bücher beträgt: {gesamt_seiten}")

for el in buch_dict:
    print(buch_dict)