import random


def losuj(ile,zIlu):
    lista = []
    i = 0

    while(i<ile):
        szczesciara = random.randint(1, zIlu)
        if szczesciara in lista:
            continue
        else:
            lista.append(szczesciara)
        i += 1

    return lista







print(losuj(5,5))
