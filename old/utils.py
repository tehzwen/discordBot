import random

def open_file(filename):
    try:
        file = open(filename, "r")
        total_lines = file.readlines()
        file.close()
        return total_lines
    
    except:
        print ("Error: Problem opening the file")
        return -1

def gambleFunc(currPoints, amount):
    randVal = random.randint(1, 100)
    win = False

    if currPoints < amount or amount < 0:
        win = None
        return win

    if randVal > 50:
        win = True

    else:
        win = False

    return win

class blackJack:
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,('J', 10), ('Q', 10), ('K', 10), ('A', 1),2,3,4,5,6,7,8,9,10,('J', 10), ('Q', 10), ('K', 10), ('A', 1)
        ,2,3,4,5,6,7,8,9,10,('J', 10), ('Q', 10), ('K', 10), ('A', 1), 2,3,4,5,6,7,8,9,10,('J', 10), ('Q', 10), ('K', 10), ('A', 1)]
        self.currentVal = 0
        self.max = 21
        self.status = None

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if type(self.cards[-1]) == int:
            self.currentVal += self.cards.pop()
            return self.currentVal
        else:
            self.currentVal += self.cards.pop()[1]
            return self.currentVal
        
    def reset_value(self):
        self.currentVal = 0

    def checkStatus(self):
        if self.currentVal == self.max:
            self.status = True
            return self.status
        
        elif self.currentVal < self.max:
            return None

        elif self.currentVal > self.max:
            self.status = False
            return self.status


def printSubreddits():
    subList = open_file('listofSubreddits.txt')
    return subList


    