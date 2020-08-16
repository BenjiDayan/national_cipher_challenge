#ABCD lock unlocker - for the question on team liquid

def sortLetterList(letter_list):
    letter_list.sort()
    #better_list contains all the characters in letter_list, just all upper
    #case and without any repeated ones.
    better_list = []
    for char in letter_list:
        if not char.upper() in better_list:
            better_list.append(char.upper())
    
    return(better_list)
    
def get_combinations(letter_list, length=False):
    '''
    Takes in a letter_list e.g. ['A','B','C','D'], removes any surplus letters.
    Then generations all the possible combinations of the list to return e.g.
    ['AAAA', 'AAAB', 'AAAC', 'AABA'...]
    '''
    better_list = sortLetterList(letter_list)

    #length can be set by the user - else it defaults to len(better_list)
    #length is the length of the desired output strings
    if not length:
        length = len(better_list)
    
    #So that combinations starts off as ['AAAA']:
    combinations = [better_list[0]*length]
    '''
    The while loop takes the last value put in combinations and starts with
    count=-1 so last value's[count] gets get_next()-ed. If this returns a
    character, a new last value is appended to combinations with this one
    character revision. If this returns false as the last value's[count] is
    alphabetically last in better_list already, count decreases by one and
    the while loop restarts to try again one letter up
    '''
    count = -1

    #the while loop finishes when all the possible combinations are used up
    #e.g. for 'ABCD' there are 4^4 possible combinations
    while len(combinations) < pow(len(better_list), length):
        next_char = get_next(combinations[-1][count], better_list)
        if not next_char:
            count -= 1
            continue
        else:
            thing = combinations[-1][:count] + next_char
            #in case count < -1 so thing isn't as long as length:
            while len(thing) < length:
                thing += better_list[0]
            combinations.append(thing)
            count = -1

    return(combinations)
            

def get_next(char, charlist):
    '''
    For use in the while loop of get_combinations to get the next value
    alphabetically along the line to put into combinations.
    if char='B' and charlist=['A','B','C','D']
    get_next returns 'C'
    '''
    if not char == charlist[-1]:
        return(charlist[charlist.index(char) + 1])
    else:
        return(False)
    

def do():
    letters = ['a','b','c','d']
    combinations = get_combinations(letters, 3)
    x = 'AAA'
    spooked = False
    while len(x) < 66:
        print(x)
        root = x[-2:]
        done = False
        for thing in combinations:
            if spooked:
                if thing[:2] == root and thing not in x:
                    spooked = False
                    continue
            if thing[:2] == root and thing not in x:
                x += thing[-1]
                done = True
                break
            
        if not done:
            done = True
            x = x[:-1]
            spooked = True
            
    return(x)        

    
    
    
