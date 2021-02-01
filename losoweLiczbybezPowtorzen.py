import random

def losoweLiczby(ile, zIlu):
    tablica = []
    i = 0

    while (i < ile):
        liczba = random.randint(1, zIlu)
        if not liczba in tablica:
            tablica.append(liczba)
            i += 1
            
    return tablica


print(losoweLiczby(3,100))
