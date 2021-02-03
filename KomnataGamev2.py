import random

def czyZnalezionoSkrzynke():
    
    wydarzenia = ("Znaleziono skrzynke","Nie znaleziono skrzynki")

    return random.choices(wydarzenia, [60, 40],  k=1)


def przyblizonaLiczba(arg, arg2):

    minliczba = arg - (arg*(arg2/100))
    
    maxliczba = arg + (arg*(arg2/100))
        
    return random.randint(minliczba,maxliczba)
    

def jakaSkrzynka():
    
    skrzynki = {"zielona": przyblizonaLiczba(1000, 10), "pomaranczowa": przyblizonaLiczba(4000, 10),
                "fioletowa": przyblizonaLiczba(9000, 10), "legendarna": przyblizonaLiczba(1600, 10)}
    
    losowanieSkrzynki = random.choices(list(skrzynki), [75, 20, 4, 1], k = 1)

    for kolor in losowanieSkrzynki:        
        return (kolor, skrzynki[kolor])

i = 5
skrzyneczki = []

while(i > 0):

    print("\n")
    
    zdarzenie = czyZnalezionoSkrzynke()
    print(zdarzenie)
    
    if(zdarzenie == ['Znaleziono skrzynke']):
        skrzyneczka = jakaSkrzynka()
        skrzyneczki.append(skrzyneczka)
        print(skrzyneczka)
    
    i -= 1


kolumnaZilosciaZlota = [y for x,y in skrzyneczki]

print("\nlacznie znalezles:", sum(kolumnaZilosciaZlota))



    
