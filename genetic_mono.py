# genetic_mono
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

english_ranking = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', \
                   'm', 'w', 'f', 'y', 'g', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z']

import random
import basics
import genetic_algorithm as ga
import math
import pickle

class node(ga.node):
    def reproduce(self, another):
        other_key = another.key
        letters_left = alphabet.copy()
        baby_key = ['' for letter in self.key]
        for num in range(len(self.key)):
            i = alphabet.index(english_ranking[num])
            a = self.key[i]
            b = other_key[i]
            if a in baby_key and b in baby_key:
                char = random.choice(letters_left)
            elif a in baby_key:
                char = b
            elif b in baby_key:
                char = a
            else:
                foo = random.randint(0, 16)
                if foo < 8:
                    char = a
                elif foo < 16:
                    char = b
                else:
                    char = random.choice(letters_left)
            letters_left.remove(char)
            baby_key[i] = char
        return(node(''.join(baby_key)))


class algorithm(ga.genetic_algorithm):
    """genetic algorithm for decrypting monoalphabetic substitution ciphers"""
    def __init__(self, text, population_size, breeding_times, node_class):
        super(type(self), self).__init__(text, population_size, breeding_times, node_class)

        # mono is the list of text's most frequent to least frequent letters
        # to be used for giving keywords a jump start
        self.mono = [x[0] for x in basics.freq_analysis(text, 1, 26)]
        for char in alphabet:
            if not char in self.mono:
                self.mono.append(char)

        self.initialize_population()

    def decrypt(self, text, key):
        return(mono_decrypt(text, key))

    def initialize_population(self):
        for num in range(self.population_size):
            self.population.append(self.node(self.make_key()))

    def make_key(self):
        # Makes a semi random, semi acording to text's most frequent letters keyword
        
        key = []
        # like standard english_ranking but with a few letters swapped
        messed_up_ranking = english_ranking.copy()
        for num in range(1):
            #Randomly swaps adjacent letters in messed_up ranking
            for index in range(25):
                if random.randint(0, 1):
                    a = messed_up_ranking[index]
                    messed_up_ranking[index], messed_up_ranking[index+1] = \
                                              messed_up_ranking[index+1], a
        
        #This would makes the ideal letter for letter for the frequency if not for
        #The messed_up_ranking being a little messed up.
        for alphanum in range(26):
            ranking_index = messed_up_ranking.index(alphabet[alphanum])
            key.append(self.mono[ranking_index])
        
        return(key)        
    
                


def mono_decrypt(text, key):
    dtext = ''
    for char in text:
        a = key.index(char)
        dtext += alphabet[a]
    return(dtext)
    
        
