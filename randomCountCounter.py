# random()              losuje liczbe x, 0 <= x < 1                         [0, 1)

# uniform(2.5, 10.0)    losuje liczbe x, 2.5 <= x < 10.0                    [2.5, 10)

# randrange(10)         losuje liczbe calkowita od 0 do 9  ->               10-1=9

# randrange(0, 15, 2)   losuje liczbe calkowita od 0 do 14, skok co 2       (0,2,4,...14)

# randint(0, 4)                                                             [0, 4]

import random

x1 = 0
while x1 < 10:                          
    x1 = x1 + 1
    print(random.random())              # RANDOM

print("------------------------")

x2 = 0
while x2 < 10:                          
    x2 = x2 + 1
    print(random.uniform(0, 100))       # UNIFORM

print("------------------------")    

def czyBronTrafi(szansaBroniNaTrafienieWprocentach):
    szansaPotrzebnaNaTrafienie = random.uniform(0, 100)
    
    if(szansaBroniNaTrafienieWprocentach > szansaPotrzebnaNaTrafienie):
        wiadomosc = (szansaBroniNaTrafienieWprocentach, "wystarczylo")
        return ['HIT', szansaPotrzebnaNaTrafienie, wiadomosc]
    else:
        wiadomosc = (szansaBroniNaTrafienieWprocentach, "nie wystarczylo")
        return ['NOT', szansaPotrzebnaNaTrafienie, wiadomosc]

x = 0
listHit = []

while x < 10:
    x = x + 1
    listHit.append(czyBronTrafi(50))                        # DODAJE LISTY które zwraca funkcja czyBronTrafi DO LISTY listHit

for zdarzenie, potrzebnaSzansa, wyjasnienie in listHit:     # WYPISUJE LISTE listHit
    print (zdarzenie, "\t", potrzebnaSzansa, "\n")
    for i in wyjasnienie:
        print(i)
    print("----------------------\n")
    
    


listHitZdarzenie = [x for x,y,z in listHit]                 # TWORZE TABLICE PIERWSZYCH ELEMENTOW TABLIC z TABLICY czyBronTrafi

print("\nilosc pudel:\t", listHitZdarzenie.count("NOT"))    #COUNT - LICZENIE ELEMENTOW LISTY
print("ilosc trafien:\t", listHitZdarzenie.count("HIT"))

from collections import Counter         

dictionaryHit = Counter(listHitZdarzenie)                   #COUNTER - LICZENIE ELEMENTOW LISTY(ZAPISANIE DANYCH JAKA WARTOSC i ILE za pomocą KLUCZ, WARTOSC do SLOWNIKA)               

print()

for x in dictionaryHit:
    print ("ilosc",x,":\t",dictionaryHit[x])

print("------------------------------------------------")

x = 0

while x < 10:
    x = x + 1
    print(random.randrange(10))

print("------------------------------------------------")


x = 0

while x < 10:
    x = x + 1
    print(random.randint(0,10))



