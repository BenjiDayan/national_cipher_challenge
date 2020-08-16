#New thought

import precipher
import solitaireCipher

text = 'aaa'
textCount = 0

missing = [2, 8, 10, 11, 12, 19, 21, 22, 26, 28, 31, 45, 46, 48, 49, 50]
#Note key now has 'a', 'b', 'c', ... , 'p' instead of all 'x'
key = [39, 35, 47, 4, 5, 42, 17, 52, 20, 13, 'A', 16, 30, 40, 38, 34, 43, 14, 41, 7, 27, 44, 1, 6, 33, 15, 'B', 36, 18, 24, 3, 9, 51, 37, 23, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 25, 'i', 'j', 'k', 'l', 'm', 'n', 32, 'o', 29, 'p']

decks = []

def eliminate(list1, list2):
    '''returns all the terms in list2 that aren't in list1'''
    for thing in list1:
        try:
            del(list2[list2.index(thing)])
        except IndexError:
            pass

class hope(solitaireCipher.Deckinator):
    def __init__(text, decisions=[], keyStream=[] deck=None ,key=''):
        '''If key is given, a deck will be made preshuffled according to it.
        Otherwise an unshuffled 1-52-a-b deck is made
        '''
        self.text = text
        self.decisions = decisions
        self.keyStream = keyStream
        deck.pass1 = False
        deck.pass2 = False
        

        temp = []
        for decision in self.decisions:
            temp.append(decision.split('=')[1])
        self.missing = eliminate(temp, missing)

        if deck:
            self.deck = deck[:]
        else:
            self.makeDeck()
            
        if key:
            self.key = key
            self.keyShuffle()

    def step2(self):
        '''Performs one complete step to return one keystream value'''
        while True:
            self.jokerShuffle()
            self.tripleCut()
            self.countCut2()
            temp = self.getOut2()
            if temp:
                break
        self.keyStream.append(temp)

    def countCut2(self):
        number = self.deck[-1]
        if type(number) is int or number == 'A' or number == 'B':
            self.countCut()
        else:
            return(number)

    def getOut2(self):
        number = self.deck[0]
        if number == 'A' or number == 'B':
            number = 53

        if not type(number) is str:
            outNum = (self.getOut())

        else:
            return([number, 'top'])

        if not outNum == 'A' and not outNum == 'B':
            if not type(outNum) is str:
                return(outNum)
            else:
                return([outNum, 'not'])
            
              

def step():
    deckCount = 0
    while deckCount < len(decks):
        while True:
            if not pass1 or pass2:
                deckinator.jokerShuffle()
                deckinator.tripleCut()

            if not pass2:
                temp = deckinator.countCut()
                if temp:
                    for number in deckinator.missing:
                        decision = temp+'='+str(number)
                        decks.append(hope(text, deckinator.decisions+decision, deckinator.keyStream)
                        decks[-1].pass1 = True
                        del(decks[deckCount])
                        deckCount -= 1
                    break

            temp = getOut2(deckinator)
            if temp and temp[1] == 'top':
                for number in deckinator.missing:
                    decision = temp[0]+'='+str(number)
                    decks.append(hope(text, deckinator.decisions+decision, deckinator.keyStream)
                    del(decks[deckCount])
                    deckCount -= 1
                b
                
