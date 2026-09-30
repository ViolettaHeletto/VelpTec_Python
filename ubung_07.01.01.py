# # Entwickle ein Python-Programm, das folgende Aufgaben erfüllt:

# a) Importiere das Modul random und das Modul time.

# b) Definiere eine Funktion wuerfeln(), die eine zufällige Zahl zwischen 1 und 6 generiert und diese zurückgibt. Verwende dafür die Funktion randint() aus dem Modul random.

# c) Definiere eine Funktion aktueller_timestamp(), die den aktuellen Unix-Timestamp zurückgibt. Verwende dafür die Funktion time() aus dem Modul time.

# d) Schreibe eine Hauptschleife, die fünfmal läuft. In jedem Durchlauf soll die Funktion wuerfeln() aufgerufen und das Ergebnis zusammen mit dem aktuellen Unix-Timestamp ausgegeben werden. Nutze dafür die Funktion aktueller_timestamp().

# e) Sorge dafür, dass zwischen jedem Würfelwurf eine Pause von 2 Sekunden liegt. Verwende dafür die Funktion sleep() aus dem Modul time. 

import random, time

def wuerfeln():
    return random.randint(1, 100)


zufallszahlen = [wuerfeln() for _ in range(10)]
print(zufallszahlen)

def sortiere_und_zähle(lst):
    lst.sort()
    return len(lst)

anzahl_elemente = sortiere_und_zähle(zufallszahlen)
#c) Liste von Tupeln erzeugen

tupel_liste = [(zahl, zahl**2) for zahl in zufallszahlen]
#d) Über Liste von Tupeln iterieren und ausgeben

for zahl, quadrat in tupel_liste:
    print(f"Die Zahl {zahl} hat das Quadrat {quadrat}")
#e) Kontrollstruktur für Anzahl der Elemente

if anzahl_elemente > 5:
    print("Mehr als 5 Elemente")
else:
    print("5 oder weniger Elemente")
