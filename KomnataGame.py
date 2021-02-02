import random

def czyZnalezionoSkrzynke():
    
    wydarzenia = ("Znaleziono skrzynke","Nie znaleziono skrzynki")
    losownieWydarzenia = random.choices(wydarzenia, [60, 40],  k=1)
    
    for wydarzenie in losownieWydarzenia:
        return wydarzenie

    

def jakaSkrzynka():
    
    skrzynki = {"zielona": 1000, "pomaranczowa": 4000, "fioletowa": 9000, "legendarna": 16000}
    losowanieSkrzynki = random.choices(list(skrzynki), [75, 20, 4, 1], k = 1)
    
    for kolor in losowanieSkrzynki:        
        return (kolor, skrzynki[kolor])

i = 5

while(i > 0):

    print("\n")
    
    x = czyZnalezionoSkrzynke()
    print(x)
    
    if(x == 'Znaleziono skrzynke'):
        for skrzynka in jakaSkrzynka():
            print(skrzynka)
            
        print("zlotych monet")
    
    i -= 1

    
