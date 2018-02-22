import random

def runSlots():
    possibilities = [':money_mouth:',':eggplant:', ':poop:',
     ':trophy:', ':alien:', ':japanese_goblin:', ':dvd:', ':pray:', ':space_invader:', ':8ball:']
    total = []

    for i in range (3):
        total.append(makeCol(possibilities))

    
    return total


def makeCol(possibilities):

    tempCol = []
    random.shuffle(possibilities)

    for i in range(3):
        tempCol.append(possibilities[i])

    return tempCol

#def printSlots(total):
    #for column in total:
        #for i in range(3):
            

def determineWin(total):
    
    if total[0][1] == total[1][1]:
        if total[1][1] == total[2][1]:
            return 1

    else:
        return 0


runSlots()