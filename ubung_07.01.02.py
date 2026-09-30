# # Entwickle ein Python-Skript, das folgende Anforderungen erfüllt:

# a) Importiere das Modul random und das Modul math.

# b) Erstelle eine Funktion namens erzeuge_zufallszahlen_liste, die zwei Parameter akzeptiert: anzahl (die Anzahl der Zufallszahlen in der Liste) und max_wert (der maximale Wert einer Zufallszahl). Die Funktion soll eine Liste von anzahl Zufallszahlen generieren, wobei jede Zufallszahl zwischen 1 und max_wert (inklusive) liegt. Nutze die Funktion randint aus dem Modul random zur Generierung der Zufallszahlen.

# c) Erstelle eine Funktion namens berechne_durchschnitt, die eine Liste von Zahlen als Parameter akzeptiert und den Durchschnittswert dieser Zahlen zurückgibt.

# d) Erstelle eine Funktion namens sortiere_und_teile, die eine Liste von Zahlen akzeptiert und die Liste in zwei Hälften teilt. Die Funktion soll zunächst die Liste aufsteigend sortieren. Dann soll die Funktion zwei Listen zurückgeben: die erste Hälfte und die zweite Hälfte der ursprünglichen Liste. Wenn die Liste eine ungerade Anzahl von Elementen hat, soll das mittlere Element zur ersten Hälfte hinzugefügt werden.

# e) Verwende die Funktion erzeuge_zufallszahlen_liste, um eine Liste mit 10 Zufallszahlen zu erzeugen, wobei max_wert 100 ist.

# f) Gib die erzeugte Liste aus.

# g) Berechne und gib den Durchschnittswert der Zufallszahlenliste mit der Funktion berechne_durchschnitt aus.

# h) Verwende die Funktion sortiere_und_teile, um die Zufallszahlenliste zu sortieren und in zwei Hälften zu teilen. Gib beide Hälften aus. 

import random, math

def erzeuge_zufallszahlen_liste(anzahl, max_wert):
    zufallszahlen_liste = [random.randint(1, max_wert + 1) for _ in range(anzahl)]
    return zufallszahlen_liste

def berechne_durchschnitt(lst):
    if not lst:  # Prüft, ob die Liste leer ist
        return None
    else:
        return sum(lst) / len(lst)

def sortiere_und_teile(lst):
    lst.sort()
    len_lst = len(lst)
    if len_lst % 2 == 0:
        halb_len = len_lst // 2
    else:
        halb_len = (len(lst) + 1) // 2 

    return lst[:halb_len], lst[halb_len:]

print(sortiere_und_teile([2, 3, 6, 7, 8, 9, 3]))

fertige_liste = erzeuge_zufallszahlen_liste(10, 100)
print(fertige_liste)
print(berechne_durchschnitt(fertige_liste))
print(sortiere_und_teile(fertige_liste))

