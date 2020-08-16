#Railfence stuff
"""
W   L   O   E   A   
 A F E F R R A F S 
  F   S   B   K   T

WLOEA AFEFR RAFSF SBKT
offset can be up to numRails*2 - 1
If we model as a count, W:0, A:1, F:2, F:3, L:0, E:1 and so on
"""

def encrypt(text, numRails, offset):
    rails = []
    for num in range(numRails):
        rails.append([])

    # count represents which step of the cycle we're at
    count = offset
    # If numRails is 3, then limit is 4, and count ranges from 0 to 3
    limit = numRails*2 - 2
    
    for num in range(len(text)):
        count = count % limit
        #-1 is the base value. abs(...) is the distance from the nadir
        rails_index = -1 -abs(count-(numRails-1))
        print('count:{0}, rails_index:{1}'.format(count, rails_index))
        rails[rails_index].append(text[num])
        count += 1

    rails_in_one = []
    for rail in rails:
        rails_in_one += rail

    return(''.join(rails_in_one))
        
        
    
