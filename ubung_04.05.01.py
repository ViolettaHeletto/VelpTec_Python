# Entwickle ein Python-Programm, das die folgenden Anforderungen erfüllt: 

# a) Das Programm soll zuerst den Benutzer bitten, eine ganze Zahl einzugeben. 
# Verwende dafür die Funktion input() und wandle die Eingabe in eine ganze Zahl um. 

# b) Überprüfe anschließend, ob die eingegebene Zahl kleiner als 10, gleich 10 oder größer als 10 ist. 
# Verwende dafür eine Kombination aus if, elif und else Anweisungen. 

# c) Für jede der drei Bedingungen soll das Programm eine entsprechende Nachricht ausgeben: 

# Wenn die Zahl kleiner als 10 ist, soll ausgegeben werden: "Die Zahl ist kleiner als 10." 

# Wenn die Zahl gleich 10 ist, soll ausgegeben werden: "Die Zahl ist genau 10." 

# Wenn die Zahl größer als 10 ist, soll ausgegeben werden: "Die Zahl ist größer als 10." 

# d) Am Ende soll das Programm eine Liste von Zahlen von 1 bis 
# zur eingegebenen Zahl (inklusive) mithilfe einer for-Schleife ausgeben. 
# Jede Zahl soll in einer neuen Zeile angezeigt werden. Verwende Kommentare im Code, 
# um die einzelnen Schritte zu erläutern. 

# Schritt 1: Benutzer nach einer Zahl fragen und Eingabe in eine ganze Zahl umwandeln

zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
# Schritt 2: Überprüfen, ob die Zahl kleiner, gleich oder größer als 10 ist

if zahl < 10:
    print("Die Zahl ist kleiner als 10.")
elif zahl == 10:
    print("Die Zahl ist genau 10.")
else:
    print("Die Zahl ist größer als 10.")
# Schritt 3: Ausgabe der Zahlen von 1 bis zur eingegebenen Zahl

for i in range(1, zahl + 1):
    print(i)
