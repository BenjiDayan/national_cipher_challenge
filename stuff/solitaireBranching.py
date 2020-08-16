#Solitaire Branching - to try to get the first 4-5 letters of the ciphertext.
import solitaireCipher
import precipher
import solitaireCipher

missing = [2, 8, 10, 11, 12, 19, 21, 22, 26, 28, 31, 45, 46, 48, 49, 50]
#Note key now has 'a', 'b', 'c', ... , 'p' instead of all 'x'
key = [39, 35, 47, 4, 5, 42, 17, 52, 20, 13, 'A', 16, 30, 40, 38, 34, 43, 14, 41, 7, 27, 44, 1, 6, 33, 15, 'B', 36, 18, 24, 3, 9, 51, 37, 23, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 25, 'i', 'j', 'k', 'l', 'm', 'n', 32, 'o', 29, 'p']

class Node():
    def __init__(self, value):
        self.value = value
        self.children = []
        #self.inheritance = inheritance
        #self.toInherit=[]

    def birth(self):
        '''Spawns an almost identical offspring - operate on it afterwards'''
        child = Node(self.value)
        self.children.append(child)

    def treeList(self):
        '''organizes nodes into a treelike list'''
        treeList = []
        treeList.append(self)
        treeList.append([child.treeList() for child in self.children])
        return(treeList)


        

def thing(node):
    for child in node.children:
        print(child)
        thing(child)


class solitaireNode(Node):
    '''
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

    def birth(self, node):
    '''

    def __init__(self, text, deck=None, children=[], key=''):
        '''If key is given, a deck will be made preshuffled according to it.
        Otherwise an unshuffled 1-52-a-b deck is made
        '''
        self.v = solitaireCipher.Deckinator(text, key=key)
        self.children = children
        self.v.text = text

        if deck:
            self.v.deck = deck
        else:
            self.v.makeDeck()
            
        if not key == '':
            self.v.key = key
            self.v.keyShuffle()

    
    def step(self):
        '''Performs one complete step to return one keystream value'''

        if len(self.children) == 0:
            while True:
                self.v.jokerShuffle()
                self.v.tripleCut()
                #Special versions of countCut and getOut
                self.countCut()
                temp = self.getOut()
                if temp:
                    break
            self.v.keyStream.append(temp)
        else:
            for child in self.children:
                child.v.step()

    def countCut(self):
        '''if the bottom card of the deck is a normal number (else clause), then
           just do normal countCut, however if it's an unkown card, then for
           each of the personalized missing numbers for self, 
        '''
        if self.v.deck[-1] in precipher.alphabet:
            temp = self[-1]
            #self.missing, as self may have already eliminated some unknown cards
            for num in self.missing:
                self.v.deck[-1] = num
                self.birth()
                self.children[-1].countCut()
                self.children.inheritance += temp+'='+str(num)
            self.v.deck[-1] = temp
            
        else:
            self.v.countCut()

    def getOut(self):
        '''Look at top card's number, goes to the index-1 of that number in the
        deck's card, and returns that card's value as output % 26
        as a top card, jokers are 53. However as an output card they are skipped
        '''
        number = self.deck[0]
        outputs = []
        if number == 'A' or number == 'B':
            number = 53

        #Extra added
        if number in precipher.alphabet:
            for possibleNum in self.missing:
                outputs.append(self.deck[possibleNum])
            return(outputs)
        
        outNum = self.deck[number]
        if not outNum == 'A' and not outNum == 'B':
            return(outNum)
        

    def get(self):
        return([self, [child.get() for child in self.children]])

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.deck)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
    
        
