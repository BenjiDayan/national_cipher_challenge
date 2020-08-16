alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

english_ranking = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', \
                   'm', 'w', 'f', 'y', 'g', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z']

import random
import math

from math import log10
import random

class mono_solver():
    def __init__(self, text):
        self.text = text
        self.dtext = text
        self.changes = {}
        self.mono = freq_analysis(text, 1, 26)
        self.tri = freq_analysis(text, 3, 26)

    def set(self, echar, dchar):
        # say that echar in text should be dchar in deciphered
        self.changes[echar] = dchar.upper()
        self.dtext = ''
        for char in self.text:
            try:
                self.dtext += self.changes[char].upper()
            except KeyError:
                self.dtext += char

        
    def getD(self):
        return(self.dtext)

    def getChanges(self):
        for key in self.changes:
            print(key + ': ' + self.changes[key].upper())



def clean(text):
    #Removes punctuation, makes everything lower case
    cleaned_text = ''
    for char in text:      
        if char.lower() in alphabet:
            cleaned_text += char.lower()
    return(cleaned_text)

def shift(text, amount):
    #Shifts the text by amount up the alphabet. If amount=1, a->b and so on.
    decrypted_text = ''
    for char in text:
        index = alphabet.index(char)
        newIndex = (index + amount) % 26
        decrypted_text += alphabet[newIndex]
    return(decrypted_text)

def freq_analysis(text, gram_length, cutoff):
    #Produces an analysis of the text in sorted list form, with gram_length
    #being the length of strings being considered (monogram, bigram, trigram..),
    #and cutoff being the maximum length of the list
    count_dict = {}
    for num in range(len(text)):
        try:
            count_dict[text[num:num + gram_length]] += 1
        except KeyError:
            count_dict[text[num:num + gram_length]] = 1

    list_dict = [[key, count_dict[key]] for key in count_dict]
    list_dict.sort(key = lambda x: x[1], reverse=True)
    return(list_dict[:cutoff])

def index_of_coincidence(text):
    # ioc is [the sum of a-z of letterfreq(letterfreq-1)]/[textlength(textlength-1)
    # variance = ioc - 1/26
    # uniform distribution ioc would be 1/26 = 0.0385
    # english text ioc would be 0.067
    count_list = freq_analysis(text, 1, 26)

    sum_thing = 0
    for thing in count_list:
        sum_thing += thing[1]*(thing[1]-1)
    length = len(text)
    return(sum_thing/(length*(length-1)))




def generate_random_text(length):
    """Generates length number of characters (lower case in alphabet) of text"""
    text = []
    for num in range(length):
        text.append(alphabet[random.randint(0, 25)])
    return(''.join(text))

def generate_english_text(length):
    try:
        start = random.randint(20, 100) * 1000
        a = war_and_peace[start:start+length]
    except NameError:
        war_and_peace = open('war_and_peace.txt')
        war_and_peace = war_and_peace.read()
        war_and_peace = clean(war_and_peace)
        start = random.randint(20*1000, 100*1000)
        a = war_and_peace[start:start+length]
    return(a)

#Use english_quadgrams.txt
class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        lines = ngramfile.readlines()
        for line in lines:
            key,count = line.split(sep)
            key = key.lower()
            self.ngrams[key] = int(count)

        # length of ngram and length of text
        self.L = len(key)
        self.N = sum(self.ngrams.values())

        # calculate log probabilities of each ngram
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text: log(ptotal) = log(p1) + log(p2) + ... '''
        score = 0
        for i in range(len(text)-self.L+1):
            """try:
                score += self.ngrams[text[i:i+self.L]]
            except KeyError:
                score += self.floor
            """
            if text[i:i+self.L] in self.ngrams:
                score += self.ngrams[text[i:i+self.L]]
            else:
                score += self.floor
            
        return(score)

class node():
    # Has a keyword that defines it's means ofo decrypting the text
    # Can breed to make a mutated offspring
    def __init__(self, keyword):
        self.keyword = keyword

    def breed(self):
        pass

class algorithm():
    #has a population of nodes with keywords, can breed to make offspring with random
    #mutations/changes, can cull to select for best english scoring offspring
    
    def __init__(self, text, population_size, breeding_times, decrypt_function):
        self.text = text
        self.breeding_times = breeding_times # how many times each parent will breed
        self.population_size = population_size
        self.population = []
        self.past_generations = []
        self.complete_scores = [] # stores the complete score history
        self.summary_scores = [] # stores min max mean median

        self.base_score = quad_scorer.score(generate_random_text(len(text)))
        self.english_score = quad_scorer.score(generate_english_text(len(text)))
		
		self.initialize_population()

    def initialize_population(self):
        # Initializes the population with size self.population, hopefully near to endpoint
        pass

    def score(self, my_node):
        return(quad_scorer.score(decrypt_function(self.text, my_node.keyword)))

    def breed(self):
        """Replaces self.population with a whole load of newly bred offspring, randomly
        selecting who pairs with who"""
        self.offspring = []
        for pop_num in range(self.population_size):
            for breed_num in range(self.breeding_times):
                self.offspring.append(self.population[pop_num].breed())

        # archive the parent generation, make the new population the offspring.
        self.past_generations.append(self.population)
        self.population = self.offspring

    def cull(self):
        """Removes the bottom scorers of the population until the population fits
        population_size"""

        # From each node in population we get [node_index, node_score] in population_ranking
        population_ranking = [[x, self.score(self.population[x])] for x in \
                              range(len(self.population))]
        population_ranking.sort(key=lambda x: x[1]) # sort by score from lowest to highest

        # The new population is the top population_size guys as ranked
        # x[0] is the index of the node
        self.population = [self.population[x[0]] for x in population_ranking[-self.population_size:]]
        # The actual scores, with the same indices as their node counterparts in population
        self.ranking = [x[1] for x in population_ranking[-self.population_size]]

        #score keeping
        self.complete_scores.append(self.ranking)
        minimum = self.ranking[0]
        maximum = self.ranking[-1]
        mean = sum(self.ranking)/self.population_size
        median = self.ranking[math.ceil(self.population_size/2)]
        self.summary_scores.append([minimum, maximum, mean, median])

class genetic_algorithm(algorithm):
    
    def breed(self):
        """Replaces self.population with a whole load of newly bred offspring, randomly
        selecting who pairs with who"""
        self.offspring = []
        # 0 will increment each time a node breeds, until it reaches breeding_times
        available = [[x, 0] for x in self.population] # who is left available
        while True:
            # take the first node in available as the base, breed them with random partners
            # in available, then remove first node from available

            # range(...) ensures we breed the right number of times
            for breed_count in range(available[0][1], self.breeding_times):
                try: # try to choose a partner from those in available
                    choice = random.choice(available[1:])
                except IndexError: #Sometimes the last guy gets left out
                    #print('ruh roh')
                    choice = [random.choice(self.population), -1]

                # breed with the chosen partner
                self.offspring.append(available[0][0].breed(choice[0]))
                # increase the partner's breed count by one
                choice[1] += 1
                # if the partner's bred the requisite number of times, remove them from available
                if choice[1] == self.breeding_times:
                    available.remove(choice)
            # remove our start node from available
            del(available[0])

            # if everyone's bred, break the loop
            if len(available) == 0:
                break

        # archive the parent generation, make the new population the offspring.
        self.past_generations.append(self.population)
        self.population = self.offspring


def mono_decrypt(text, keyword):
	"""Takes text that has been encrypted with keyword, and returns it to normal text"""
	dtext = ''
	for char in text:
		dtext += alphabet[keyword.index(char)]
		
	return(dtext)
		
		
"""

def markov_generator(text, order):
    # order is how many characters back are we looking at
    ngram_to_state_dict = {}
    for num in range(len(text) - order + 1):
        try:
            ngram_to_state_dict[text[num:num+order]] += 1
        except

class markov_state():
    def __init__(self):
        #here data is the state's tri or whatever gram
        self.links = {}
        self.link_count = 0 #For generating probability

    def reinforce_link(self, linked_state):
        # where linked_state is another markov_state, and we're trying to build links
        try:
            self.links[linked_state] += 1
        except KeyError:
            self.links[linked_state] = 1

        self.link_count += 1

    def make_probDir(self):
        # Takes accumulated links, and converts to a probability dictionary
        for key in self.links:
            self.links[key] = self.links[key]/self.link_count

    def get_probability(self, key):
        # Returns the probability value of "key" in the probability dictionary
        return(self.links[key])

"""

file = open('C:\\Users\\benjamin\\Documents\\python\\national_cipher_challenge_pytwo\\english_quadgrams.txt')
quad_scorer = ngram_score(file)
        
        
