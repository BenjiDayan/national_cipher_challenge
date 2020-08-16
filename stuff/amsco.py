#Amsco

def split(string, first=True):
    splitList = []
    numList = []
    temporary = list(string)
    length = len(string)
    toggle = 0
    if not first:
        toggle = 1
    while sum(numList) < length:
        if len(temporary) > 1:
            numList.append(toggle + 1)
            for num in range(toggle + 1):
                del(temporary[0])

        else:
            numList.append(1)

        toggle = ((toggle + 1)%2)

    print(numList)
        
    stringCount = 0
    numCount = 0
    while stringCount < len(string):
        splitList.append(string[stringCount:stringCount+numList[numCount]])
        stringCount += numList[numCount]
        numCount += 1

    return(splitList)


def isEnglish(text):
    """gets all the quadgrams, compiles their probability, and compares
    that probability to normal english"""
    quadList = []
    count = 0
    while count <= len(text)-4:
        quadList.append(text[count:count + 4])
        count += 1

    occurenceList = []
     

    return(quadList)
        
    
    
    
