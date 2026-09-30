# a) Definiere eine Funktion namens temperatur_umrechner, 
# die zwei Parameter akzeptiert: temperatur und einheit. 
# Der Parameter einheit soll optional sein und standardmäßig den Wert 'C' für Celsius haben. 
# Die Funktion soll die Temperatur von Celsius in Fahrenheit umrechnen, 
# wenn einheit den Wert 'C' hat, und von Fahrenheit in Celsius, wenn einheit den Wert 'F' hat. 
# Die Umrechnungsformeln lauten: (C = (F - 32) * 5/9) und (F = C * 9/5 + 32).

# b) Verwende eine while-Schleife, um vom Benutzer wiederholt Temperaturen und 
# optional die Einheiten einzulesen, bis der Benutzer entscheidet, das Programm zu beenden. 
# Gib für jede Eingabe die umgerechnete Temperatur aus. 
# Implementiere eine Möglichkeit für den Benutzer, 
# das Programm durch Eingabe eines bestimmten Wortes, zum Beispiel "ende", zu beenden.

# c) Stelle sicher, dass dein Programm Fehleingaben 
# (wie z.B. nicht-numerische Temperaturwerte oder falsche Einheitsangaben) elegant behandelt, 
# indem du entsprechende Fehlermeldungen ausgibst und den Benutzer zur erneuten Eingabe aufforderst. 

def temperatur_umrechner(temperatur, einheit='C'):
    if einheit == 'C':
        temperatur = (temperatur * 9)/5 + 32
    elif einheit == 'F':
        temperatur = (temperatur - 32) *5/9
    else:
        print('Input ist nicht korrekt')
        # raise ValueError('Einheit muss C oder F sein')
    return temperatur


def check_value_float (message):
    # Loop until the user provides a valid number
    while True: 
        try:
            # Try to convert the input to a float
            return float(input(message))
        except ValueError:
            # If conversion fails, the input was not a number
            print("Your number isn't a number")



temperatur_input = check_value_float('Enter temperatur: ')
einheit_input = input('Enter einheit (C, F, oder nichts): ').upper() or 'C'
temperatur_output = temperatur_umrechner(temperatur_input, einheit_input)
print(f'Ergebnis: {temperatur_output}')



# def temperatur_umrechner(temperatur, einheit='C'):
#     if einheit == 'C':
#         return temperatur * 9/5 + 32
#     elif einheit == 'F':
#         return (temperatur - 32) * 5/9
#     else:
#         return None
# while True:
#     eingabe = input("Gib eine Temperatur mit Einheit ein (z.B. '35 C' oder '95 F'), oder 'ende' zum Beenden: ")
#     if eingabe.lower() == 'ende':
#         break
#     try:
#         teile = eingabe.split()
#         temp = float(teile[0])
#         if len(teile) == 2:
#             einheit = teile[1].upper()
#         else:
#             einheit = 'C'  # Standardwert, wenn keine Einheit angegeben ist
#         umgerechnet = temperatur_umrechner(temp, einheit)
#         if umgerechnet is not None:
#             if einheit == 'C':
#                 print(f"{temp} °C entspricht {umgerechnet} °F")
#             else:
#                 print(f"{temp} °F entspricht {umgerechnet} °C")
#         else:
#             print("Bitte gib eine gültige Einheit ('C' oder 'F') ein.")
#     except ValueError:
#         print("Bitte gib eine gültige Zahl für die Temperatur ein.")
#     except Exception as e:
#         print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
