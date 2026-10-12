# Entwickle ein Python-Programm, das folgende Funktionalitäten umfasst:
import re
import json

# a) Lese einen Text aus einer Datei, die Unicode-Zeichen enthält, 
# und speichere den Text in einer Variablen. Verwende dazu die 
# with-Anweisung und stelle sicher, dass die Datei korrekt geschlossen wird.

def lese_text (dateiname):
    try:
        with open(dateiname, mode='r', encoding='utf-8') as datei:
            text = datei.read()
            return text
    except FileNotFoundError:
        print(f"Die Datei {dateiname} wurde nicht gefunden.")


# b) Verwende reguläre Ausdrücke, um alle Wörter im Text zu finden, 
# die mit einem Großbuchstaben beginnen, und speichere diese Wörter in einer Liste.

def finde_grossbuchstaben_wörter(text):
    return re.findall(r'\b[A-ZÄÖÜ][a-zäöüß]*', text)

#re.findall(r'\b[^\W\d_][^\W\d_]*', text)  # любые буквы


# c) Erstelle eine Funktion, die die Anzahl der Vorkommen jedes Wortes in der Liste aus b) zählt 
# und diese in einem Dictionary speichert.

def zähle_wörter(worter):
    wort_zähler = {}
    for wort in worter:
        if wort in wort_zähler:
            wort_zähler[wort] += 1
        else:
            wort_zähler[wort] = 1
    return wort_zähler


# d) Speichere das Dictionary aus c) in einer JSON-Datei. Stelle sicher, 
# dass Umlaute und Sonderzeichen korrekt gespeichert werden.
def speichere_als_json(dict, jsonname):
    with open(jsonname, 'w', encoding='utf-8') as jsonstream:
        json.dump(dict, jsonstream, ensure_ascii=False, indent=4)

# e) Lies die JSON-Datei, die du in d) erstellt hast, und gib 
# den Inhalt in der Konsole aus. 
# Verwende hierbei die richtige Kodierung, um Umlaute und Sonderzeichen korrekt darzustellen.
def lese_json(dateiname):
    with open(dateiname, 'r', encoding='utf-8') as datei:
        inhalt = json.load(datei)
        print(inhalt)

text = lese_text('tagebuch.txt')
wörter = finde_grossbuchstaben_wörter(text)
wort_zähler = zähle_wörter(wörter)
print(wort_zähler)
speichere_als_json(wort_zähler, 'wort_zähler.json')
lese_json('wort_zähler.json')
