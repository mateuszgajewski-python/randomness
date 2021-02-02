import random

cardList = ["9","9","9","9",
            "10","10","10","10",
            "J","J","J","J",
            "Q","Q","Q","Q",
            "K","K","K","K"]

random.shuffle(cardList)

def pobierz5kart(lista, name1, name2, name3, name4):
    slownik = {name1: [], name2: [], name3: [], name4: []}
    for x in slownik:
        tablica = []
        for y in range(0,5):
           karta = cardList.pop()
           tablica.append(karta)
        slownik[x] = tablica

    return slownik
       
       

    #return lista
'''

kartyGraczy = []

for x in range(0,4):
    gracz = pobierz5kart(cardList)
    kartyGraczy.append(gracz)

for gracz in kartyGraczy:
    print(gracz)
    


for karta1,karta2,karta3,karta4, karta5 in kartyGraczy:
    print(karta1,karta2,karta3,karta4,karta5)
'''
kartyDlaGraczy = pobierz5kart(cardList, "ania", "kasia", "janek", "adam")

for key in kartyDlaGraczy:
    print(key, kartyDlaGraczy[key])
