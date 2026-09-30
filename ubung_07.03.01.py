# Aufgabe:  Kollektionen
# Entwickle ein Python-Programm, das folgende Funktionalitäten umfasst:

# a) Importiere das Modul random und das Modul math. Verwende aus dem Modul random die Funktion randint und aus math die Funktion sqrt.

# b) Erstelle eine Funktion erzeuge_zufallszahlen_liste(n), die eine Liste mit n zufälligen ganzen Zahlen zwischen 1 und 100 zurückgibt.

# c) Erstelle eine Funktion berechne_wurzeln(liste), die für jede Zahl in der übergebenen Liste die Quadratwurzel berechnet und die Wurzeln in einer neuen Liste speichert. Gib diese Liste zurück.

# d) Erstelle eine Funktion sortiere_und_erzeuge_tupel(liste), die die Liste von Quadratwurzeln aufsteigend sortiert und ein Tupel aus (Originalzahl, Quadratwurzel) für jede Zahl in der ursprünglichen Liste erzeugt. Speichere diese Tupel in einer Liste und gib sie zurück.

# e) Erstelle eine Funktion erstelle_dictionary(tupel_liste), die ein Dictionary erstellt, wobei der Schlüssel die Originalzahl und der Wert die Quadratwurzel ist. Gib dieses Dictionary zurück.

# f) Verwende alle oben erstellten Funktionen in einer Hauptfunktion main(), um eine Liste mit 10 zufälligen Zahlen zu erzeugen, die Quadratwurzeln zu berechnen, die Liste zu sortieren, das Tupel zu erstellen und schließlich das Dictionary zu erstellen und auszugeben.

# g) Gib am Ende des Programms das erstellte Dictionary aus. 

import random, math

def erzeuge_zufallszahlen_liste(n):
    zufallszahlen_liste = [random.randint(1, 100) for _ in range(n)]
    return zufallszahlen_liste

def berechne_wurzeln(liste):
    wurzel_list = [math.sqrt(x) for x in liste if x >= 0]
    return wurzel_list

def sortiere_und_erzeuge_tupel(liste):
    paar_list = [(zahl, math.sqrt(zahl)) for zahl in liste]
    paar_list.sort(key=lambda x: x[1])
    return paar_list

def erstelle_dictionary(tupel_liste):
    return {tupel[0]: tupel[1] for tupel in tupel_liste}

lst = [25, 125, 121, 64, 9, 16]
print(lst)
print(sortiere_und_erzeuge_tupel(lst))
print(erstelle_dictionary(sortiere_und_erzeuge_tupel(lst)))



def main():                                       # ← вот она
    zahlen = erzeuge_zufallszahlen_liste(10)
    wurzeln = berechne_wurzeln(zahlen)
    tupel_liste = sortiere_und_erzeuge_tupel(zahlen)
    dict_ = erstelle_dictionary(tupel_liste)
    print("Zahlen:      ", zahlen)
    print("Wurzeln:     ", wurzeln)
    print("Tupel-Liste: ", tupel_liste)
    print("Dictionary:  ", dict_)


if __name__ == "__main__":                        # ← и вот
    main()
