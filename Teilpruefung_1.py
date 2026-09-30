# Entwickle ein Python-Programm, das als Taschenrechner 
# für einfache mathematische Operationen 
# (Addition, Subtraktion, Multiplikation, Division) fungiert. 
# Das Programm soll den Benutzer zuerst fragen, 
# welche Operation durchgeführt werden soll. 
# Anschließend fragt es nach zwei Zahlen, führt die gewählte Operation mit diesen Zahlen durch und
# gibt das Ergebnis aus. Beachte dabei die korrekte Anwendung von Datentypen,
# die Implementierung von Kontrollstrukturen sowie die korrekte Verwendung von Kommentaren im Code. 

# a) Fordere den Benutzer auf, eine Operation auszuwählen, 
# indem er einen der folgenden Buchstaben eingibt: 
# A für Addition, 
# S für Subtraktion, 
# M für Multiplikation, 
# D für Division.

# b) Frage den Benutzer nach zwei Zahlen.

# c) Führe die ausgewählte Operation mit diesen Zahlen durch und gib das Ergebnis aus.

# d) Implementiere eine Fehlerbehandlung für den Fall, 
# dass bei der Division durch Null versucht wird oder ein ungültiger Operator eingegeben wird.

# e) Verwende Kommentare im Code, um die Logik hinter 
# den einzelnen Schritten zu erklären. 


def calculator (operation, first_number, second_number):
    result  = 0
    # Addition: add the two numbers
    if operation == 'A':
        result  = first_number + second_number
        print(f'Your result: {first_number} + {second_number} = {result }')
     # Subtraction: subtract the second number from the first
    elif operation == 'S':
        result  = first_number - second_number
        print(f'Your result: {first_number} - {second_number} = {result }')
    # Multiplication: multiply the two numbers
    elif operation == 'M':
        result  = first_number * second_number
        print(f'Your result: {first_number} * {second_number} = {result }')
    # Division: divide the first number by the second
    elif operation == 'D':
        # Check for division by zero before performing the division
        if second_number != 0:
            result  = first_number/second_number
            print(f'Your result: {first_number} : {second_number} = {result }')
        else:
            print("Division by zero is not allowed. Please enter another number.")
    # Fallback in case an unknown operator is passed to the function
    else:
        print("Unknown operation.")
    return result 


def check_operator ():
    # Loop until the user provides a valid operator
    while True: 
        # Read input, convert to uppercase to accept both 'a' and 'A'
        operation = input('Enter the operation ( A für Addition, S für Subtraktion, M für Multiplikation, D für Division.): ').upper()
        # Check whether the operation exists
        if operation in ('A', 'S', 'M', 'D'):
            return operation
        else : 
            # Inform the user about the invalid input and ask again
            print('You have selected a non-existent option.')


def check_value (message):
    # Loop until the user provides a valid number
    while True: 
        num_input = input(message)
        try:
            # Try to convert the input to a float
            value = float(num_input)
            return value
        except ValueError:
            # If conversion fails, the input was not a number
            print("Your number isn't a number")


# Step 1: Ask the user which operation to perform
operator = check_operator()

# Step 2: Ask the user for the first number
first_number = check_value('Enter the first number: ')

# Step 3: Ask the user for the second number
second_number = check_value('Enter the second number: ')

# Step 4: Perform the chosen operation and print the result
calculator(operator, first_number, second_number)
