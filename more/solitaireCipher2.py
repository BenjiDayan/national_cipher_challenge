#Solitaire cipher v2.0
#Note 'a' represents little joker, 'b' big joker. 'a' is shifted down one,
#'b' shifted two when keyShuffling, and when generating the keystream.

import precipher #for precipher.alphabet

class Deckinator():

    deck = []
    key = ''
    keyStream = []

    def __init__(self, key=''):
        '''If key is given, a deck will be made preshuffled according to it.
        Otherwise an unshuffled 1-52-a-b deck is made
        '''
        self.makeDeck()
        if not key == '':
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

    def getKeyStream(self, length):
        '''Generates a keystream of length number of digits'''
        for num in range(length):
            done = False #incase getOut() returns None as a joker is hit
            temp = []
            while not done:
                self.jokerShuffle()
                self.tripleCut()
                self.countCut()
                temp.append(self.getOut())
                if temp[-1]:
                    done = True
            self.keyStream.append(temp[-1])

    def decrypt(self, text):
        '''Generates an appropriately long keyStream, then decrypts the text by
        minusing the values in the keyStream from the values in the text % 24.
        '''
        self.keyStream = []
        self.getKeyStream(len(text))
        dtext = ''
        for num in range(len(text)):
            a = precipher.alphabet.index(text[num])
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

    
    
    
    
    
