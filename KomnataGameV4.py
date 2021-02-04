import random

from enum import Enum

jezyk = input("podaj jezyk ang / pol")

if jezyk == "pol":

    Wydarzenie = Enum('Wydarzenie',{'JEST_SKRZYNKA': 'HURA, ZNALAZLES SKRZYNKE',
                                    'NIE_MA_SKRZYNKI': 'NIC TU NIE MA'}
                 )

    DictWydarzenie = {
                        Wydarzenie.JEST_SKRZYNKA: 60,
                        Wydarzenie.NIE_MA_SKRZYNKI: 40
                    }

    #########################################################################

    Skrzynka = Enum('Skrzynka', {'zielona': 'ZIELONA SKRZYNECZKA',
                                 'pomaranczowa': 'POMARANCZOWA SKRZYNECZKA',
                                 'fioletowa': 'FIOLETOWA SKRZYNECZKA',
                                 'zlota': 'ZLOTA SKRZYNECZKA'})

    DictKolorSkrzynki = {
                            Skrzynka.zielona: 75,
                            Skrzynka.pomaranczowa: 20,
                            Skrzynka.fioletowa: 4,
                            Skrzynka.zlota: 1
                        }

    ##########################################################################




elif jezyk == "ang":

    Wydarzenie = Enum('Wydarzenie',{'JEST_SKRZYNKA': 'I FIND A BOX',
                                    'NIE_MA_SKRZYNKI': 'THERE IS NOTHING'}
                 )

    DictWydarzenie = {
                        Wydarzenie.JEST_SKRZYNKA: 60,
                        Wydarzenie.NIE_MA_SKRZYNKI: 40
                    }

    #########################################################################

    Skrzynka = Enum('Skrzynka', {'zielona': 'GREEN BOX',
                                 'pomaranczowa': 'ORANGE BOX',
                                 'fioletowa': 'VIOLET BOX',
                                 'zlota': 'GOLD BOX'})

    DictKolorSkrzynki = {
                            Skrzynka.zielona: 75,
                            Skrzynka.pomaranczowa: 20,
                            Skrzynka.fioletowa: 4,
                            Skrzynka.zlota: 1
                        }

    ##########################################################################








DictWartoscSkrzynki = {
                        Skrzynka.zielona: 1000,
                        Skrzynka.pomaranczowa: 4000,
                        Skrzynka.fioletowa: 9000,
                        Skrzynka.zlota: 16000
                    }

listWydarzenieKlucze = list(DictWydarzenie.keys())
listWydarzeniePrawdopodobienstwo = list(DictWydarzenie.values())

listKolorSkrzynkiKlucze = list(DictKolorSkrzynki.keys())
listKolorSkrzynkiPrawdopodobienstwo = list(DictKolorSkrzynki.values())

y = 5
nagroda = 0

while(y>0):

    wylosowaneWydarzenie = random.choices(listWydarzenieKlucze,listWydarzeniePrawdopodobienstwo)[0]
    print(wylosowaneWydarzenie.value)
    
    if(wylosowaneWydarzenie == Wydarzenie.JEST_SKRZYNKA):
                       
        wylosowanyKolorSkrzynki = random.choices(listKolorSkrzynkiKlucze,listKolorSkrzynkiPrawdopodobienstwo)[0]
        print(wylosowanyKolorSkrzynki.value)
        nagroda = DictWartoscSkrzynki[wylosowanyKolorSkrzynki]
        print(nagroda)

    

        
    
    print("\n")
    y -= 1
