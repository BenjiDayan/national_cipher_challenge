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

def caesarSolve(text):
    '''
    Returns deciphered version of the caesar encrypted "text"
    '''

    shift = findShift(text)

    #Remember to reverse the shift, we must shift by -shift.
    dtext = precipher.alphaShift(text, -shift)
    return(dtext)
