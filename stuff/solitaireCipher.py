#Solitaire cipher
#Note 'a' represents little joker, 'b' big joker. 'a' is shifted down one,
#'b' shifted two when keyShuffling, and when generating the keystream.

import precipher #for precipher.alphabet
missing = [2, 8, 10, 11, 12, 19, 21, 22, 26, 28, 31, 45, 46, 48, 49, 50]
#Note key now has 'a', 'b', 'c', ... , 'p' instead of all 'x'
key = [39, 35, 47, 4, 5, 42, 17, 52, 20, 13, 'A', 16, 30, 40, 38, 34, 43, 14, 41, 7, 27, 44, 1, 6, 33, 15, 'B', 36, 18, 24, 3, 9, 51, 37, 23, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 25, 'i', 'j', 'k', 'l', 'm', 'n', 32, 'o', 29, 'p']


class Deckinator():

    deck = []
    key = ''
    keyStream = []

    def __init__(self, text, deck=None, key=''):
        '''If key is given, a deck will be made preshuffled according to it.
        Otherwise an unshuffled 1-52-a-b deck is made
        '''
        self.text = text

        if deck:
            self.deck = deck
        else:
            self.makeDeck()
            
        if key:
            self.key = key
            self.keyShuffle()

    def makeDeck(self):
        '''Initializes the deck from top (start) to bottom (end) with
        1, 2, 3, ... 52, a, b
        '''
        self.deck = [x for x in range(1, 53)]
        self.deck.append('A')
        self.deck.append('B')

    def keyShuffle(self, key):
        '''Shuffles up the deck according to the key
        '''
        for char in key:
            self.jokerShuffle()
            self.tripleCut()
            self.countCut()
            self.countCut(char)

    def getKeyStream(self):
        '''Generates a keystream of length number of digits'''
        for num in range(len(self.text)):
            #incase step() returns None as getOut() hits a joker
            self.step()

    def step(self):
        '''Performs one complete step to return one keystream value'''
        while True:
            self.jokerShuffle()
            self.tripleCut()
            self.countCut()
            temp = self.getOut()
            if temp:
                break
        self.keyStream.append(temp)

    def decrypt(self):
        '''Generates an appropriately long keyStream, then decrypts the text by
        minusing the values in the keyStream from the values in the text % 24.
        '''
        self.keyStream = []
        self.getKeyStream()
        dtext = ''
        for num in range(len(self.text)):
            a = precipher.alphabet.index(self.text[num])
            b = self.keyStream[num]
            c = (a-b)%26
            dtext += precipher.alphabet[c]
                
        return(dtext)
            

    def jokerShuffle(self):
        aIndex = self.deck.index('A')
        shiftElement(self.deck, aIndex, 1)

        bIndex = self.deck.index('B')
        shiftElement(self.deck, bIndex, 2)

    def tripleCut(self):
        '''Swaps the cards on either side of the two jokers.
        246 B 5871 A 39    becomes
        39 B 5871 A 246
        If A and B are opposite sides of the deck, then there is no change.
        A 1234 B    stays the same.
        '''

        aPos = self.deck.index('A')
        bPos = self.deck.index('B')
        if aPos < bPos:
            firstPos = aPos
            secondPos = bPos
        else:
            firstPos = bPos
            secondPos = aPos

        midSection = self.deck[firstPos:secondPos+1]
        pre = self.deck[:firstPos]
        post = self.deck[secondPos+1:]
        self.deck = post + midSection + pre

    def countCut(self, number=0):
        '''Looks at the bottom card's number, moves all cards from beginning
        up to but not including that number's index to just before the bottom
        card (to ensure that you can reverse easily?)
        so [1,4,2,5,3]
        becomes [5,1,4,2,3]

        Includes functionality for countCutting by key, in which case give an
        argument which is the key character for number.
        '''

        # number=0, bool(number) = False - do normal countCut
        if not number:
            # Assign number as the value of the bottom card of deck
            number = self.deck[-1]
            if number == 'A' or number == 'B':
                number = 53

        # number=letter, bool(number) = True - do countCut with key character
        else:
            # Assign number according to key char. Note 'a' is 1 not 0
            number = precipher.alphabet.index(number) + 1

        pre = self.deck[:number]
        mid = self.deck[number:-1]
        self.deck = mid + pre + [self.deck[-1]]
        
        
    def getOut(self):
        '''Look at top card's number, goes to the index-1 of that number in the
        deck's card, and return's that card's value as output % 26
        as a top card, jokers are 53. However as an output card they are skipped
        '''
        number = self.deck[0]
        if number == 'A' or number == 'B':
            number = 53

        #Added
        if number == 'x':
            return('#')

        #Extra added
        if number in precipher.alphabet:
            outputs = []
            for possibleNum in missing:
                outputs.append(self.deck[possibleNum])
            return(outputs)
        
        outNum = self.deck[number]
        if not outNum == 'A' and not outNum == 'B':
            return(outNum)

    
        

    

def cut(myList, index):
    '''swaps all the elements before, not including the index element to the end
    of the list, and so the elment of index becomes the beginning of the list.
    '''
    previouslyBeginning = myList[:index]
    previouslyEnd = myList[index:]
    print(previouslyEnd + previouslyBeginning)
    thing = previouslyEnd + previouslyBeginning
    print(thing)
    myList = thing


def shiftElement(myList, index, shiftAmount):
    '''For simulating jokerShuffling. Does the following operation:
    takes out the elment in myList at index 'index', then places it along by
    shiftAmount. If the element would be placed out of the end of the list,
    it wraps around back to the other end, placed one in from the edge as if
    the whole were a circle
    '''

    eachHop = 1
    if shiftAmount < 0:
        eachHop = -1

    temporary = myList[index]
    del(myList[index])
    insertionPoint = index

    for num in range(abs(shiftAmount)):
        insertionPoint += eachHop
        if insertionPoint == len(myList) + 1 and eachHop == 1:
            insertionPoint = 1
        elif insertionPoint == -1 and eachHop == -1:
            insertionPoint = len(myList) - 1

    myList.append('temp')
    myList.insert(insertionPoint, temporary)
    del(myList[-1])

    
    
    
    
    
