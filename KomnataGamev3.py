import random

from enum import Enum


def findApproximateValue(value):
    lowestValue = value - 0.1 * value
    highestValue = value + 0.1 * value
    return random.randint(lowestValue, highestValue)



#####################################################################

Event = Enum('Event',['Chest', 'Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                 }

eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

#####################################################################


Colours = Enum('Colours', ['Green','Orange','Purple','Gold']
               )

chestColoursDictionary = {
                            Colours.Green: 0.75,
                            Colours.Orange: 0.2,
                            Colours.Purple: 0.04,
                            Colours.Gold: 0.01
                        }
                            

chestColoursList = tuple(chestColoursDictionary.keys())
chestColoursProbability = tuple(chestColoursDictionary.values())

#####################################################################


rewardsForChests = {
                        Colours.Green: 1000,
                        Colours.Orange: 4000,
                        Colours.Purple: 9000,
                        Colours.Gold: 16000
                    }





gameLength = 5

while gameLength > 0:
    gamerAnswer = input("enter")

    drawEvent = random.choices(eventList, eventProbability)[0]
    
    if (drawEvent == Event.Chest):
        print("CHEST")
        
        drawnColor = random.choices(chestColoursList, chestColoursProbability)[0]
        print(drawnColor)
        
        cash = findApproximateValue(rewardsForChests[drawnColor])
        print (cash)
        
    elif (drawEvent == Event.Empty):
        print("EMPTY")

   

    gameLength = gameLength - 1
                    
