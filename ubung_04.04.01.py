#Entwickle ein Python-Programm, 
# das die Rolle eines einfachen Quizspiels übernimmt. 
# Das Spiel soll aus drei Fragen bestehen, 
# die nacheinander gestellt werden.
# Für jede Frage gibt es drei Antwortmöglichkeiten (a, b, c), 
# von denen genau eine richtig ist. Nachdem der Spieler alle Fragen beantwortet hat, 
# soll das Programm die Anzahl der richtig beantworteten Fragen ausgeben und eine Rückmeldung geben.
#  Verwende für jede Frage eine if-elif-else-Struktur, um zu überprüfen, ob die Antwort des Spielers richtig 
# oder falsch ist. Nutze zudem eine while-Schleife, um sicherzustellen, dass das Spiel nur fortgesetzt wird, 
# wenn der Spieler eine gültige Antwort (a, b, oder c) eingegeben hat.
#  Wenn eine ungültige Eingabe erfolgt,
#  soll der Spieler erneut zur Eingabe aufgefordert werden, 
# bis eine gültige Antwort gegeben wird.

question1 = 'Which planet in our solar system is known as the Red Planet?'
antwort11 = 'a) Mars'
antwort12 = 'b) Venus'
antwort13 = 'c) Jupiter'
question2 = 'What is the capital city of the United Kingdom?'
antwort21 = 'a) Edinburgh'
antwort22 = 'b) London'
antwort23 = 'c) Manchester'
question3 = 'Which famous playwright wrote the tragedy "Romeo and Juliet"?'
antwort31 = 'a) William Shakespeare'
antwort32 = 'b) Charles Dickens'
antwort33 = 'c) Mark Twain'

richtig = 'Ja, dein Antwort ist richtig'
falsch = 'Nein, leider dein Antwort ist nicht richtig'
ergebnis = 0
input_true = False

print("Erste Frage ist:", question1)
print(antwort11)
print(antwort12)
print(antwort13)
while not input_true : 
    aktion = input("Wähle einen Antwort: 'a', 'b' oder 'c': ")
    if aktion in ('a', 'b', 'c'):
        input_true = True
        if aktion == 'a':
            print(richtig)
            ergebnis += 1
        else :
            print(falsch)
    else : 
        print('You have selected a non-existent option.')

input_true = False
print("Zweite Frage ist:", question2)
print(antwort21)
print(antwort22)
print(antwort23)
while not input_true : 
    aktion = input("Wähle einen Antwort: 'a', 'b' oder 'c': ")
    if aktion in ('a', 'b', 'c'):
        input_true = True
        if aktion == 'b':
            print(richtig)
            ergebnis += 1
        else :
            print(falsch)
    else : 
        print('You have selected a non-existent option.')

input_true = False
print("Dritte Frage ist:", question3)
print(antwort31)
print(antwort32)
print(antwort33)
while not input_true : 
    aktion = input("Wähle einen Antwort: 'a', 'b' oder 'c': ")
    if aktion in ('a', 'b', 'c'):
        input_true = True
        if aktion == 'a':
            print(richtig)
            ergebnis += 1
        else :
            print(falsch)
    else : 
        print('You have selected a non-existent option.')

print(f"Dein Ergebnis ist: {ergebnis}/3")



# рекомендации от Deepseek:

# def stelle_frage(frage, a1, a2, a3, richtige_antwort):
#     print(frage)
#     print(a1)
#     print(a2)
#     print(a3)
#     while True:
#         aktion = input("Wähle eine Antwort: 'a', 'b' oder 'c': ")
#         if aktion in ('a', 'b', 'c'):
#             if aktion == richtige_antwort:
#                 print("Deine Antwort ist richtig.")
#                 return 1
#             else:
#                 print("Leider falsch.")
#                 return 0
#         else:
#             print("Ungültige Eingabe, bitte erneut versuchen.")

# ergebnis = 0

# ergebnis += stelle_frage(
#     'Which planet is known as the Red Planet?',
#     'a) Mars', 'b) Venus', 'c) Jupiter',
#     'a'
# )

# ergebnis += stelle_frage(
#     'What is the capital of the United Kingdom?',
#     'a) Edinburgh', 'b) London', 'c) Manchester',
#     'b'
# )

# ergebnis += stelle_frage(
#     'Who wrote "Romeo and Juliet"?',
#     'a) William Shakespeare', 'b) Charles Dickens', 'c) Mark Twain',
#     'a'
# )

# print(f"Dein Ergebnis ist: {ergebnis}/3")