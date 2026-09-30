# # Erstelle ein Python-Programm, das folgende Aufgaben erfüllt:

# a) Importiere das Modul random und verwende eine Funktion aus diesem Modul, um eine Zufallszahl zwischen 1 und 10 zu generieren. Speichere diese Zahl in einer Variablen.

# b) Definiere eine Funktion namens berechne_quadrat, die einen Parameter nimmt, dessen Quadrat berechnet und das Ergebnis zurückgibt.

# c) Verwende eine if-Kontrollstruktur, um zu überprüfen, ob die generierte Zufallszahl größer als 5 ist. Falls ja, rufe die Funktion berechne_quadrat mit der Zufallszahl als Argument auf und gib das Ergebnis aus. Falls nein, gib eine Nachricht aus, die besagt, dass die Zahl kleiner oder gleich 5 ist.

# d) Implementiere eine Schleife, die von 1 bis zur generierten Zufallszahl läuft und dabei jedes Mal die aktuelle Zahl ausgibt. 

import random
# Generiere eine Zufallszahl zwischen 1 und 10

zufallszahl = random.randint(1, 10)
# Definiere die Funktion berechne_quadrat

def berechne_quadrat(zahl):
    return zahl * zahl
# Überprüfe, ob die Zufallszahl größer als 5 ist

if zufallszahl > 5:
    ergebnis = berechne_quadrat(zufallszahl)
    print(f"Das Quadrat von {zufallszahl} ist {ergebnis}.")
else:
    print(f"Die Zahl {zufallszahl} ist kleiner oder gleich 5.")
# Implementiere eine Schleife, die von 1 bis zur generierten Zufallszahl läuft

for i in range(1, zufallszahl + 1):
    print(i)
