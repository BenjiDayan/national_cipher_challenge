#Railfence cipher solver

#One easyish way to solve a railfence cipher seems to be to use the same
#encryption to jumble up a list of numbers [0, 1, 2, 3, ...] of the same length
#as the encrypted text, then use the resultant jumbled letters as a key to
#unscramble the ciphertext

def railfence(text, rails, reverse=False):
    '''Takes text as the plaintext and rails as the number of rails, then
    arranges the text accordingly
    e.g. rails = 3
    a   e   i   m    and so on, then rearranges this into 
     b d f h j l     "aeim...bdfhjl...cgk..."
      c   g   k
    '''

    rows = []
    for num in range(rails):
        rows.append('')

   #Goes through each letter in text, adding each to right row in rows 
    marker = 0    #the current rail (out of 0, 1, 2... ,rails-1)
    down = True   #whether you're journeying down the rail or up 
    count = 0     #the position in text you're at
    while count < len(text):
        char = text[count]
        rows[marker] += char

        
        if down:
            marker += 1
        else:
            marker -= 1

        if marker == -1 :
            marker = 1
            down = not down
        elif marker == rails:
            marker = rails - 2
            down = not down

        count += 1

    #reverse is for if for some reason the rail looks like an M instead of a W
    if reverse == True:
        rows.reverse()
    return(rows)


    
        
        
        
