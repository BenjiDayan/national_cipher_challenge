'''
Allows scoring of text using n-gram probabilities
17/07/12
'''
from math import log10

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        lines = ngramfile.readlines()
        for line in lines:
            key,count = line.split(sep)
            key = key.lower()
            self.ngrams[key] = int(count)

        # length of ngram and length of text
        self.L = len(key)
        self.N = sum(self.ngrams.values())

        # calculate log probabilities of each ngram
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text: log(ptotal) = log(p1) + log(p2) + ... '''
        score = 0
        for i in range(len(text)-self.L+1):
            try:
                score += self.ngrams[text[i:i+self.L]]
            except KeyError:
                score += self.floor          
        return score
       
