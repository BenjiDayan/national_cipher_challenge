#hill2

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

def decrypt_text2(text, key):
    dm1m26 = key.T % 26
    new = (key * dm1m26).T

    length = len(key)
    chunks = split(text, length)
    comp = ''
    for num in range(math.ceil(len(text)/length)):
        comp += convert_chunk(chunks[num], key)

    return(comp)
    

def decrypt_text(text, key):
    length = len(key)
    chunks = split(text, length)
    chunknums = [chunk_to_num(chunk) for chunk in chunks][:-1]
    posses = []
    for numpair in chunknums:
        posses.append(solve_equation([key[0][0], key[0][1], numpair[0]], [key[1][0], key[1][1], numpair[1]]))

    return(posses)
    comp = ''
    for thing in posses:
        for mini in thing:
            comp += basics.alphabet[mini[0]]

    return(comp)

def solve2(eq1, eq2):
    e1, e2 = np.array(eq1), np.array(eq2)
                                 

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
    thnum = chunk_to_num(th)
    henum = chunk_to_num(he)
    poss1 = solve_equation([19, 7, thnum[0]], [7, 4, henum[0]])
    poss2 = solve_equation([19, 7, thnum[1]], [7, 4, henum[1]])
    return(poss1 + poss2)

def solve_equation(eq1, eq2):
    """Takes in e.g. eq1 = [q, w, e], eq2 = [r, t, y] where
    qa + wb = e mod(26) and ra + tb = y mod(26). Returns values of  a and b
    """
    e1, e2 = solve_half_p1(eq1, eq2), solve_half_p1([eq1[1], eq1[0], eq1[2]], [eq2[1], eq2[0], eq2[2]])

    aposs, bposs = find_possibilities(e1[0], e1[2]), find_possibilities(e2[0], e2[2])
    return([aposs, bposs])

def solve_half_p1(eq1, eq2):
    #Works by elimination
    e1, e2 = np.array(eq1), np.array(eq2)   
    e1x = e1 * e2[1]
    e2x = e2 * e1[1]
    e3 =  (e1x - e2x) % 26
    return(e3)

def find_possibilities(a, b):
    """Given ax = b mod(26), finds possibilities for a and b"""
    prac = np.array([x for x in range(26)])
    prac *= a
    prac = prac % 26
    indices = []
    for index in range(26):
        if prac[index] == b:
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
