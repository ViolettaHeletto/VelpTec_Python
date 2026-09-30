# Entwickle ein Python-Programm, das eine Funktion namens berechne_durchschnitt definiert,
# welche eine Liste von Zahlen als Parameter akzeptiert und den Durchschnittswert dieser Zahlen zurückgibt. 
# Dein Programm sollte folgende Anforderungen erfüllen:

# a) Definiere die Funktion berechne_durchschnitt, die eine Liste von Zahlen entgegennimmt. 
# Die Funktion soll den Durchschnitt dieser Zahlen berechnen und das Ergebnis zurückgeben.

# b) Verwende eine for-Schleife innerhalb der Funktion, um durch die Liste zu iterieren und 
# die Summe der Zahlen zu berechnen.

# c) Außerhalb der Funktion, definiere eine Liste von Zahlen und weise sie einer Variablen zu. 
# Verwende dann diese Liste als Argument, um die Funktion berechne_durchschnitt aufzurufen.

# d) Gib das Ergebnis des Funktionsaufrufs mit einer aussagekräftigen Nachricht 
# mithilfe der print()-Funktion aus.

# e) Stelle sicher, dass dein Programm auch mit einer leeren Liste umgehen kann, 
# ohne einen Fehler zu verursachen. 
# In diesem Fall soll die Funktion None zurückgeben. 



def berechne_durchschnitt(zahlen_liste):
    if not zahlen_liste:  # Prüft, ob die Liste leer ist
        return None
    summe = 0
    for zahl in zahlen_liste:
        summe += zahl
    durchschnitt = summe / len(zahlen_liste)
    return durchschnitt
# Liste von Zahlen definieren
zahlen = [10, 20, 30, 40, 50]
# Funktion aufrufen und Ergebnis ausgeben
durchschnitt = berechne_durchschnitt(zahlen)
if durchschnitt is not None:
    print(f"Der Durchschnitt der Zahlenliste ist: {durchschnitt}")
else:
    print("Die Liste ist leer.")
# Beispiel mit einer leeren Liste
leere_liste = []
durchschnitt_leer = berechne_durchschnitt(leere_liste)
if durchschnitt_leer is not None:
    print(f"Der Durchschnitt der leeren Liste ist: {durchschnitt_leer}")
else:
    print("Die Liste ist leer.")