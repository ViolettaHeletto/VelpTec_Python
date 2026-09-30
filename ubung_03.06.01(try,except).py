#a) Schreibe ein Python-Skript, das eine Liste von Ganzzahlen definiert 
# und die Summe sowie den Durchschnitt dieser Zahlen berechnet.
# Kommentiere jeden Schritt deines Skripts, um zu erklären, was gemacht wird.

#diffinition list of int
int_list = [4, 5, 8, 1, 3]
int_sum = 0
quantity_el = 0
for element in int_list:
    int_sum += element
    quantity_el += 1
    print(element)

print("Summa of elements: ", int_sum)
print("Quantity of elements: ", quantity_el)

arith_mean = int_sum / len(int_list)
#arith_mean = int_sum / (quantity_el)
print("Arith mean of elements: ", arith_mean)


#b) Erstelle ein Python-Skript, das eine Zeichenkette (String) 
# von einem Benutzer einliest und anschließend prüft, ob es sich um eine Ganzzahl (int) 
# oder eine Gleitkommazahl (float) handelt. 
# Gib das Ergebnis aus und erkläre den Prozess in Kommentaren.


num_input = input('Enter a number: ')

try: 
    value = int(num_input)
    print("Your number is int")

except ValueError:
    try:
        value = float(num_input)
        print("Your number is float")
    except ValueError:
        print("Your number isn't a number")


print("Willkommen zum Fehlerfindungs-Quiz!")
zahl1 = float(input("Bitte gib eine Zahl ein: "))
zahl2 = float(input("Bitte gib eine andere Zahl ein: "))
ergebnis = zahl1 + zahl2
print("Das Ergebnis der Addition ist: ", ergebnis)