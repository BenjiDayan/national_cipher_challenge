#log probability

import pickle
import math

#occurences = pickle.load( open( "warOnPeace.p", "rb" ) )
#logProbs = pickle.load( open( "logProbs.p", "rb" ) )
logProbsDir = pickle.load( open( "logProbsDir.p", "rb" ) )


def getProb(text):
    quadgrams = {}
    for num in range(len(text)-5):
        quadgram = text[num:num+4]
        if quadgram not in quadgrams:
            quadgrams[quadgram] = 1
        else:
            quadgrams[quadgram] += 1

    newList = []
    for key in quadgrams:
        newList.append([key, quadgrams[key]])

    
    probability = 0
    for thing in newList:
        if thing[0] in logProbsDir:
            probability += thing[1]*logProbsDir[thing[0]]
        else:
            probability += -15

    return(probability)
