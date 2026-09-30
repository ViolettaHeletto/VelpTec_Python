# Entwickle ein Python-Programm, das eine Datenanalyse für ein fiktives Unternehmen durchführt, 
# welches verschiedene Produkte verkauft. Deine Aufgabe besteht darin, eine Reihe von Funktionen zu erstellen, 
# die verschiedene Analysen ermöglichen. Das Programm soll folgende Funktionen beinhalten:
# # 

# d) Eine Funktion preis_mit_steuer, die den Preis eines Produkts inklusive Mehrwertsteuer berechnet. 
# Die Funktion nimmt zwei Argumente: den Preis ohne Steuer und den Steuersatz 
# (als optionalen Parameter mit einem Default-Wert von 19%).

# e) Eine Lambda-Funktion, die zusammen mit der map()-Funktion verwendet wird, 
# um die Preise einer Liste von Produkten um einen bestimmten Prozentsatz zu erhöhen. 
# Die Prozentsatzerhöhung soll als Argument übergeben werden.

# f) Eine Funktion drucke_produktliste, die eine Liste von Produktnamen schön formatiert 
# auf der Konsole ausgibt. Verwende die print()-Funktion, um jedes Produkt in einer neuen Zeile auszugeben. 
# Liste an Produkten:

# Laptop, 999,00€

# Smartphone, 599,00€

# Kopfhörer, 149,00€

# Smartwatch, 249,00€

# Tablet, 399,00€

# E-Book-Reader, 129,00€

# Fitness-Tracker, 79,00€

# Bluetoothlautsprecher, 89,00€

# Powerbank, 39,00€

# Webcam, 59,00€

# a) Eine Funktion durchschnittspreis, die den Durchschnittspreis aus einer Liste von Produkt-Preisen berechnet. 
# Die Funktion nimmt eine Liste von Preisen als Argument und gibt den Durchschnittspreis zurück.
def durchschnittspreis(preis_list):
    dspreis = 0
    summa = 0
    for el in preis_list:
        summa += el
    dspreis = summa/len(preis_list)
    return dspreis

# b) Eine Funktion produkt_filter, die eine Liste von Produktnamen und einen Buchstaben 
# als Argumente nimmt und alle Produkte zurückgibt, die mit diesem Buchstaben beginnen, unter Verwendung der filter()-Funktion.
def produkt_filter(name_list, buchstaben):
    produkte_mit_buchstaben = []
    for el in name_list:
        if buchstaben in el[0]:
            produkte_mit_buchstaben.append(el)
    return produkte_mit_buchstaben

# c) Eine rekursive Funktion max_preis, die den höchsten Preis in einer Liste von Preisen findet. 
# Wenn die Liste leer ist, soll die Funktion None zurückgeben.
def max_preis(preis_list):
    if not preis_list:
        return None
    preis = preis_list[0]          
    for el in preis_list[1:]:
        if preis < el:
            preis = el
    return preis

# def max_preis(preis_list):
#     return max(preis_list) if preis_list else None

# def max_preis(preise):
#     if not preise:
#         return None
#     if len(preise) == 1:
#         return preise[0]
#     else:
#         max_rest = max_preis(preise[1:])
#         return preise[0] if preise[0] > max_rest else max_rest

produkt_preisen = [ 599, 149, 249, 399, 129, 999, 79, 89, 39, 59]
produkt_namen = ['Laptop', 'Smartphone', 'Kopfhörer', 'Smartwatch', 'Tablet', 'E-Book-Reader', 
                 'Fitness-Tracker', 'Bluetoothlautsprecher', 'Powerbank', 'Webcam']
 
mittelpreis = durchschnittspreis(produkt_preisen)
print(f'Das Durchschnittspreis ist: {mittelpreis}')
buchstabe_input = input('Geben Sie einen Buchstaben ein, nach dem sortiert werden soll:').upper()

namen_ergebnis = produkt_filter(produkt_namen, buchstabe_input) 
if namen_ergebnis:
    print(f'Ergebnis fur Ihre Suche ist: {namen_ergebnis}')
else:
    print('Sorry, es gibt kein Ergebnis.')

print(f'Maximal Preis ist: {max_preis(produkt_preisen)}')

def preis_mit_steuer(preis, steuersatz=19):
    return preis * (1 + steuersatz / 100)

def erhoehe_preise(preise, prozentsatz):
    return list(map(lambda preis: preis * (1 + prozentsatz / 100), preise))
# 2. list comprehension (питоничнее)
# [preis * (1 + prozentsatz / 100) for preis in preise]

def drucke_produktliste(produkte):
    for produkt in produkte:
        print(produkt)
