#choice - zwraca losowy element
#choices - zwraca liczbe elementow i ma wieksze mozliwosci

import random

movieList = ["Tytul 1", "Tytul 2", "Tytul 3", "Tytul 4"]

event = ["smierc", "wygrana", "przegrana", "utrata zlota", "utrata zycia"]

nagrodaZeSkrzynki = ["zielona", "pomaranczowa", "purpurowa", "legendarna"]

print(random.choice(movieList))

print("--------------------------------")

print(random.choice(nagrodaZeSkrzynki))

print("--------------------------------")

print(random.choices(nagrodaZeSkrzynki))

print("--------------------------------")

print(random.choices(nagrodaZeSkrzynki, k = 100))

print("--------------------------------")

from collections import Counter

DictColours = (Counter(random.choices(nagrodaZeSkrzynki, [4, 1, 0.25, 0.1] , k = 100)))

print(DictColours)

for x in DictColours:
    print(x[:-1], "ych jest:", DictColours[x])


               
      
