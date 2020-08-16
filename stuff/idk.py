#New Solitaire for decisions

import solitaireCipher
import precipher

class idk(solitaireCipher.Deckinator):

    def countCut2(self, number=0):
        try:
            self.countCut()
        except TypeError:
            return self.deck[-1]

    def getOut2(self):
        number = self.deck[0]
        if number == 'A' or number == 'B':
            number = 53

        if type(number) is str:
            return([number, 'Top'])

        outNum = self.deck[number]
        if type(outNum) is str:     
            if not outNum == 'A' and not outNum == 'B':
                return([outNum, 'Not'])
            else:
                return(None)

        else:
            return(outNum)
            
