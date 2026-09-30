anzahl = 5
size = 10.2
komplex = 5+3j
name = 'Violetta'

print("Der Datentyp von ganze_zahl ist:", type(anzahl))
print("Der Datentyp von kommazahl ist:", type(size))
print("Der Datentyp von komplexe_zahl ist:", type(komplex))
print("Der Datentyp von zeichenkette ist:",type(name))

sum_int_float = anzahl + size
print(type(sum_int_float))

name += " - Python Basics"
print(name)
print(type(name))