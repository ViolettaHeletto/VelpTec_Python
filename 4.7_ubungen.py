#Dabei ist m das Körpergewicht in kg, h die Körpergröße in cm und a das Alter in
# Jahren. Schreibe ein interaktives Programm mit einer Fallunterscheidung, das
# den Grundumsatz berechnet.

male = input('Enter your male (m/f): ')
grundumsatz = 0

if male not in ('m', 'f'):
    print('Please write m or f.')
else:
    alter = int(input('Enter your alter: '))
    weight = float(input('Enter your weight: '))
    height = float(input('Enter your height: '))
    if male == 'm':
        grundumsatz = 66.5 + 13*weight + 5*height - 6.8*alter
        print('Your grundumsatz is: ', grundumsatz)
    elif male == 'f':
        grundumsatz = 66.5 + 13*weight + 5*height - 6.8*alter
    print('Your grundumsatz is: ', grundumsatz)

