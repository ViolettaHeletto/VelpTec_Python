# # Aufgabe: Module
# a) Gebe an, wie du das Modul math in Python importierst und verwende eine Funktion aus diesem Modul, 
# um die Quadratwurzel von 256 zu berechnen.

# b) Erstelle eine Variable radius mit dem Wert 7. 
# Berechne den Umfang eines Kreises unter Verwendung der Variable radius und der Konstante pi aus dem Modul math. 
# Schreibe das Ergebnis in eine neue Variable umfang und gib sie aus.

# c) Beschreibe, wie du eine eigene Funktion namens fahrenheit_zu_celsius definierst, 
# die eine Temperatur in Fahrenheit entgegennimmt und die entsprechende Temperatur in Celsius zurückgibt. 
# Verwende diese Funktion anschließend, um die Temperatur 68°F in Celsius umzurechnen und das Ergebnis auszugeben.

# d) Erkläre, wie eine einfache for-Schleife in Python aussieht, 
# die die Zahlen von 1 bis einschließlich 5 ausgibt. Verwende dazu eine Schleife und die print-Funktion.

# e) Benenne die zwei grundlegenden Arten, wie Funktionen aus Modulen in 
# Python importiert werden können, und gib für jede Art ein Beispiel an.

import math

quadratwurzel = math.isqrt(25)
print(quadratwurzel)

radius = 7
kreis = 2 * math.pi * radius
print(kreis)

def fahrenheit_zu_celsius(tmp_F):
    return (tmp_F * 9)/5 + 32

temperatur_in_F = float(input('Enter temp: '))
print(fahrenheit_zu_celsius(temperatur_in_F))

for i in range(1, 6):
    print(i)