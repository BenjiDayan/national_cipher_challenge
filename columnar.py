#Columnar transposition cipher
import math
import basics

def standard_split(text, row_length):
    """text = abcdefghijklmnopqrstuvwxyz and row_length = 5
    abcde
    fghij
    klmno
    pqrst
    uvwxy
    z      returns ['afkpuz', 'bglqv', 'chmrw', 'dinsx', 'ejoty']
    """
    output = []
    text_length = len(text)
    # Takes output column by index in turn, taking e.g. the 0th, 5th, 10th ... char
    # for the 0th column, then the 1st, 6th, 11th ... char for the 1st column etc.
    for num in range(row_length):
        count = num
        output.append([])
        while count < text_length:
            output[-1].append(text[count])
            count += row_length

    return(output)

def tricky_split(text, row_length):
    """text = afkpuzbglqvchmrwdinsxejoty and row_length = 5
    abcde
    fghij
    klmno
    pqrst
    uvwxy
    z      returns ['afkpuz', 'bglqv', 'chmrw', 'dinsx', 'ejoty']
    """
    output = []
    text_length = len(text)
    over_shoot = text_length % row_length #e.g. 26 % 5 = 1
    shortest_col_length = math.floor(text_length/row_length) # e.g. 5
    index_count = 0 #for keeping track of position
    for num in range(row_length):
        if num < over_shoot: #aka we're still in overshoot zone
            output.append(text[index_count:index_count + shortest_col_length+1])
            index_count += shortest_col_length + 1
        else:
            output.append(text[index_count:index_count + shortest_col_length])
            index_count += shortest_col_length

    return(output)

def decolumnify(columns):
    """Takes ['afkpuz', 'bglqv', 'chrmw', 'dinsx', 'ejoty']
    and outputs abcdefghijklmnopqrstuvwxyz
    """
    comp = ''
    keyword_length = len(columns)
    for row_num in range(len(columns[0])):
        for column_num in range(keyword_length):
            try:
                comp += columns[column_num][row_num]
            except IndexError:
                pass
    return(comp)
    

def shuffle_columns(columns, keyword, encrypt=True):
    """Takes in columns like ['afkpuz', 'bglqv', 'chmrw', 'dinsx', 'ejoty']
    and keyword like [3, 1, 0, 4, 2], and if encrypt=True
    returns the shuffled by the keyword columns, otherwise the unshuffled
    (like decrypting)
    """

    # Each column e.g. 'afkpuz' becomes ['afkpuz', x], where x is the destination
    # column index of 'afkpuz'

    shuffled_columns = columns.copy()

    if not encrypt:
        keyword = invert_keyword(keyword)
    
    for num in range(len(keyword)):
        shuffled_columns[num] = [columns[num], keyword.index(num)]

    shuffled_columns.sort(key = lambda x: x[1])
    for num in range(len(shuffled_columns)):
        shuffled_columns[num] = shuffled_columns[num][0]

    return(shuffled_columns)


     
def invert_keyword(keyword):
    """Takes in a keyword e.g. [3, 1, 0, 2], which describes the mapping of
    abcd to dbac, and returns the keyword that returns dbac to abcd. So if
    you have a keyword that encrypts a text, the decrypting keyword woud be
    its inverse and vice versa
    """

    # for each index of the inv_keyword, find the position of that index in
    # keyword, and have that as the value, in order to reorder the text.
    # So keyword = [3, 1, 0, 2], we want [2, 1, 3, 0] to return normalcy
    
    inv_keyword = [keyword.index(index) for index in range(len(keyword))]
    return(inv_keyword)
    
    


    
