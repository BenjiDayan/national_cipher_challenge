
import basics
import genetic_algorithm as ga
import math
import numpy as np
import random


""" Hill Cipher - uses a matrix as a key, and splits text into small chunks 
        [1, 2, 3] ['a'][1]   [14]           ['n']
        [4, 5, 6] ['b'][2] = [32] mod(26) = ['f']
        [7, 8, 9] ['c'][3]   [50]           ['x']
"""

def encrypt_text(text, key_matrix):
    """Returns the encrypted by key_matrix text"""

    length = len(key_matrix)
    chunks = split(text, length)
    comp = ''
    for num in range(math.ceil(len(text)/length)):
        comp += convert_chunk(chunks[num], key_matrix)

    return(comp)

def decrypt_text(text, key_matrix):
    length = len(key_matrix)
    chunks = split(text, length)
    chunknums = [chunk_to_num(chunk) for chunk in chunks]
    eqs = []
    for nums in chunknums:
        eqs.append([[key_matrix[0][0], key_matrix[0][1], nums[0]], [key_matrix[1][0], key_matrix[1][1], nums[1]]])

    return(eqs)

def decrypt(text, key):
    length = len(key)
    chunks = split(text, length)
    chunknums = [chunk_to_num(chunk) for chunk in chunks][:-1]
	
    solutions = []
    for num in chunknums:
        sola = get_half([[key[0][0], key[0][1], num[0]], [key[1][0], key[1][1], num[1]]])
        solb = get_half([[key[0][1], key[0][0], num[0]], [key[1][1], key[1][0], num[1]]])
	
        solutions.append(sola)
        solutions.append(solb)
		
    return(solutions)
    
def split(text, length):
    """Splits the text into chunks of length length, returning the list of
    chunks e.g. text='abcdefghi', length=3 -> ['abc', 'def', 'ghi']
    If the text isn't long enough, the last chunk might be shorter
    """
    chunks = []
    count = 0
    iterations = math.floor(len(text)/length)
    while count < iterations:
        chunks.append(text[length*count : length*(count+1)])
        count += 1

    #Catches the tail end which might be shorter than length
    chunks.append(text[length*count:])
    if len(chunks[-1]) > 0: #If there was some leftover
        for num in range(length-len(chunks[-1])):#pad with 'a' as necessary
            chunks[-1] += 'a'
    return(chunks)


def convert_chunk(chunk, key_matrix):
    a = np.array([basics.alphabet.index(letter) for letter in chunk])
    b = np.dot(key_matrix, a)
    b = b % 26
    comp = ''.join([basics.alphabet[int(index)] for index in b])
    return(comp)

def chunk_to_num(chunk):
    return([basics.alphabet.index(char) for char in chunk])

def get_key(th, he):
	eqs = get_equations(th, he)
	solved = [solve_equation(eqs[num]) for num in range(2)]
	return(np.array(solved))

def get_equations(th, he):
    """Takes in the suspected cipher text for th and he, key length 2. spits
    out the equations"""
    foo1 = chunk_to_num(th)
    foo2 = chunk_to_num(he)
    goo1 = chunk_to_num('th')
    goo2 = chunk_to_num('he')

    #ab is of the form [[q, w, e], [r, t, y]], where qa + wb = e mod(26), ra + tb = y mod(26)
    ab = [goo1 + [foo1[0]], goo2 + [foo2[0]]]
    cd = [goo1 + [foo1[1]], goo2 + [foo2[1]]]
    return([ab, cd])

def solve_equation(eq):
    """eq is of the form [[q, w, e], [r, t, y]], where qa + wb = e mod(26), ra + tb = y mod(26)
    returns [a, b]"""
    a = get_half(eq)
    b = get_half([[x[1], x[0], x[2]] for x in eq])
    return(a, b)

def get_half(eq):
    e1, e2 = np.array(eq[0]), np.array(eq[1])
    #Aim to eliminate b
    e1x = e1*e2[1]
    e2x = e2*e1[1]

    e3 = (e1x - e2x) % 26
    prac = np.array([x for x in range(26)])
    prac *= e3[0]
    prac = prac % 26
    return(arr_find(e3[2], prac))
    
   # return(e3[0] * e3[2]) % 26
    

def arr_find(element, arr):
    indices = []
    for index in range(len(arr)):
        if arr[index] == element:
            indices.append(index)
    return(indices)
    
    
    

class hill_cipher_node(ga.node):
    def reproduce(self, another):
        #Returns a node, whose keyword is a breeding of self and another's 
        length = len(self.key)
        baby_key = np.zeros([length, length], int)
        for rownum in range(length):
            for colnum in range(length):
                if random.randint(0, 1):
                    out = self.key[rownum][colnum]
                else:
                    out = self.key[rownum][colnum]

                if random.randint(0, 12) == 12:
                    out = random.randint(0, 25)

                baby_key[rownum][colnum] = out
        return(hill_cipher_node(baby_key))

class hill_cipher_algorithm(ga.genetic_algorithm):
    def __init__(self, text, population_size, breeding_times, node_class, key_matrix_side_length):
        super(type(self), self).__init__(text, population_size, breeding_times, node_class)
        self.key_matrix_side_length = key_matrix_side_length
        self.initialize_population()
        
    def decrypt(self, text, key):
        return(encrypt_text(text, key))

    def initialize_population(self):
        for num in range(self.population_size):
            self.population.append(self.node(self.make_key(self.key_matrix_side_length)))

    @staticmethod
    def make_key(length):
        key = np.zeros([length, length], int)
        for rownum in range(length):
            for colnum in range(length):
                key[rownum][colnum] = random.randint(0, 25)

        return(key)
                
        
            
            
        
        
