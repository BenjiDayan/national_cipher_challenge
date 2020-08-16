#caesar cipher solver

import precipher

def findShift(text):
    '''
    Returns how much a caesar ciphered text has been shifted.
    '''

    #The most popular letter's index in the alphabet is 'epos'.
    epos = precipher.alphabet.index('e')

    #Gets common letters in "stats", "ourpos" index of the letter E,
    #And the "shift" amount between "ourpos" and "epos".
    stats = precipher.popular(text, 1, 3)
    ourpos = precipher.alphabet.index(stats[0][0])
    shift = ourpos - epos

    return(shift)

def monoShift(text, preletter, postletter):
    """inputted a cleaned text, outputs a version of the text where the lower
    case versions of preletter are replaced with uppercase postletters"""

class monoShifter():
    """eases solving monoalphabetic substitution ciphers"""

    
    
    def __init__(self, text):
        #self.text stores the cleaned text for reference, self.editedText
        #stores the current version of the edited text
        self.text = list(precipher.clean(text))
        self.editedText = list(precipher.clean(text))

        #replacements stores letter swaps in format postLetter:preLetter.
        #This format is for ease of finding a postLetter's preLetter when
        #calling undo (which reverts a postLetter to a preLetter)
        self.replacements = {}

    def replace(self, preLetter, postLetter):
        """Replaces lowercase preletters with uppercase postletters"""
        self.replacements[postLetter] = preLetter
        self.monoShift(preLetter, postLetter)

    def monoShift(self, preLetter, postLetter):
        """inputted a cleaned text, outputs a version of the text where the lower
        case versions of preletter are replaced with uppercase postletters
        WARNING: make sure preLetter and postLetter are lowercase"""
        for num in range(len(self.editedText)):
            if self.editedText[num] == preLetter:
                self.editedText[num] = postLetter.upper()

    def undo(self, postLetter):
        """undoes the replacement that caused postLetter's existence
        WARNING: postLetter should be lowercase"""
        #Tries to find more capital postLetters. If can find no more, all
        #of the undoing is done, so exits.
        while True:
            try:
                #num is the index of the next postLetter to undo
                num = self.editedText.index(postLetter.upper())
            except ValueError:
                del(self.replacements[postLetter])
                return

            self.editedText[num] = self.replacements[postLetter]

    def gt(self):
        """Returns self.text in string format"""
        return(''.join(self.text))
    def ge(self):
        """Returns self.editedText in string format"""
        return(''.join(self.editedText))
        
        
        
        
    
        
def isolate(text, length):
    """tries to find a length long string in text with specified letters"""
    indices = []
    for num in range(len(text)-length+1):
        temp = text[num:num+length]
        had = []
        for letter in temp:
            if not letter in had:
                had.append(letter)
        if len(had) == length:
            indices.append(num)

    return(indices)
    

def caesarSolve(text):
    '''
    Returns deciphered version of the caesar encrypted "text"
    '''

    shift = findShift(text)

    #Remember to reverse the shift, we must shift by -shift.
    dtext = precipher.alphaShift(text, -shift)
    return(dtext)

class vigenereSolver():

    text = ''
    #sepText is the storage of the untampered with separated characters
    sepText = []
    #data stores the popular monograms for each block in sepText
    data = []

    #topSep contains the shifted versions of each block in sepText for the top
    #monograms for each block in sepText
    topSep = []
    #topSepData contains the popular monograms for each variant of each block
    #in topSep
    topSepData = []

    #outSep contains the chosen variants from topSep, and is designated for
    #unseparation into plaintext
    outSep = []
    #out is the finished product
    out = ''

    def __init__(self, text):
        self.text = text

    def getDifferences(self, ngram):
        self.positions = position(ngram, self.text)
        self.differences = difference(self.positions)
        print(self.differences)

    def separate(self, num):
        self.sepText = separate(self.text, num)
        for block in self.sepText:
            self.data.append(precipher.popular(block, 1, 26))
            self.topSep.append([])
            for num in range(3):
                self.topSep[-1].append(\
                precipher.alphaShift(block, -findShift(self.data[-1][num][0])))

        for block in self.topSep:
            self.topSepData.append([])
            for variant in block:
                self.topSepData[-1].append(precipher.popular(variant, 1, 26))

    def chooseVariant(self):
        choice = []
        for block in self.topSepData:
            for variant in block:
                print(variant)
                print()

            choice.append(int(input("Type 0, 1 or 2 >    ")))
            print()

        for num in range(len(choice)):
            self.outSep.append(self.topSep[num][choice[num]])

        self.out = ''.join(unseparate(self.outSep))
        
                        
    


def position(ngram, text):
    '''
    Finds the positions of all occurrences of the ngram in the text.
    Returns a list with the indexes of the starts of these positions.
    '''

    length = len(ngram)
    positions = []
    for num in range(len(text)):
        if text[num: num+length] == ngram:
            positions.append(num)
    return(positions)

def difference(positions):
    '''
    Returns the differences between the positions in position
    '''
    differences = []
    for num in range(len(positions)):
        if num+1 < len(positions):
            differences.append(positions[num+1] - positions[num])
    return(differences)

def separate(text, numSets):
    '''
    Seperates the text into numSets of almost equal length lists
    of characters.

    Within text:
    1st char to 1st set
    2nd char to 2nd set
    ...
    numSets char to numSets set
    numSets+1 char to numSets+1 set
    ...
    '''

    sets = [[] for num in range(numSets)]

    #Going through each character of the text - position represented
    #By "count". "setNumCount" keeps going up until it hits numSets
    #Then back down to 0.
    count = 0
    setNumCount = 0
    while count < len(text):
        if setNumCount == numSets:
            setNumCount = 0
        sets[setNumCount].append(text[count])
        count += 1
        setNumCount += 1

    return(sets)

def unseparate(separated):
    copy = separated
    for num in range(len(copy)):
        copy[num] = list(copy[num])
    joined = []
    count = 0
    while True:
        try:
            type(copy[count][0])
        except IndexError:
            break
        joined.append(copy[count][0])
        del(copy[count][0])
        count += 1
        if count == len(separated):
            count = 0
    return(joined)

def solve(text, keylength, option=False):
    separated = separate(text, keylength)
    separatedSolved = []
    for num in range(len(separated)):
        separatedSolved.append(list(caesarSolve(separated[num])))
    if option:
        return(separatedSolved)
    unseparatedSolved = unseparate(separatedSolved)
    return(''.join(unseparatedSolved))
    
