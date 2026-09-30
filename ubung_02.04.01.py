meineFreunde = ["Lisa", "Bart", "John", "Eddy", "Kate"]
print(meineFreunde)

# zweiNeueFreunde = ["Ben", "Rita"]
meineFreunde.append("Ben")
meineFreunde.append("Rita")
print(meineFreunde)

meineFreunde.remove("Ben")
print(meineFreunde)

int_tupel = (4, 7, 5)
a = (list(int_tupel), 6, 2)
print(a) 

frucht_set = {'apfel', 'banane', 'ananas' }
frucht_set.add("orange")
print(frucht_set)

landDictionary = {'Deutschland':'Berlin',
                  'England':'London',
                  'Italien':'Rom'
                  }
print(landDictionary)
