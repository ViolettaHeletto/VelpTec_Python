# Entwickle eine Python-Funktion namens filtere_gerade_zahlen, 
# die eine Liste von Zahlen als Argument nimmt und mithilfe der filter()-Funktion 
# alle geraden Zahlen aus dieser Liste zurückgibt. Verwende eine Lambda-Funktion, 
# um zu bestimmen, ob eine Zahl gerade ist. Die Funktion soll die gefilterten Zahlen als Liste zurückgeben. 
# Teste deine Funktion mit einer Liste von Zahlen und gib das Ergebnis mit der print()-Funktion aus. 
# Verwende für deine Tests die Liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# und stelle sicher, dass deine Funktion korrekt implementiert ist, indem du das Ergebnis überprüfst. 

zahlen_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtere_gerade_zahlen(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

print(f'Gerade Zahlen: {filtere_gerade_zahlen(zahlen_liste)}')