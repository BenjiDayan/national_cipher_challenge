#Practice - do some simple cipher functions

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alphaShift(myString, shift):
    '''
    In Caesar shift style shifts every letter in myString along by shift amount.
    >>> alphaShift('abc', 2)
    'cde'
    '''
    shift = shift % 26
    newString = ''
    for char in myString:
        newString += alphabet[(alphabet.index(char) + shift) % 26]

    return(newString)
    
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],         
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def clean(myString):
    '''
    Removes all spaces, punctuation and capitals from myString
    '''
    newString = ''
    for char in myString:
        if char.lower() in alphabet:
            newString += char.lower()
    return(newString)


def popular(myString, strLength, limit):
    '''
    Finds the 'limit' most common ministrings in myString, descending.
    Returns a list where each element is [ministring, occurenceCount].
    strLength is the length of ministring to search for e.g. 3 letters

    >>> popular(myString, 3, 5)
    [['the', 20], ['and', 14], ['tha', 10], ['ate', 8], ['oot', 2]]

    '''

    # mydir will contain string:occurences for every strLength string.
    mydir = {}
    for index in range(len(myString) - strLength + 1):
        try:
            mydir[myString[index:index + strLength]] += 1
        except KeyError:
            mydir[myString[index:index + strLength]] = 1

    # Now to turn mydir into a list and sort by most occurences first.
    mylist = []
    for thing in mydir:
        mylist.append([thing, mydir[thing]])

    mylist.sort(key=lambda x: x[1], reverse=True)
    mylist = mylist[:limit]
    return(mylist)



def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.                          

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''                                                                     
    if size < 0:
        raise ValueError('number must be non-negative')                     

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)                       

    raise ValueError('number too large')
