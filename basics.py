alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

english_ranking = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', \
                   'm', 'w', 'f', 'y', 'g', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z']

file = open('unique_words.txt', 'r')
stuff = file.read()
unique_words = stuff.split('\n')
del(stuff)
file.close()

import pickle
import random
import math
import cProfile
import pstats

from math import log10
import random
import matplotlib.pyplot as plt

file = open('google-10000-english.txt', 'r')
stuff = file.read()
common_words = stuff.split('\n')
file.close()
del(stuff)

def is_rare(word, limit):
    return(not word in common_words[:limit])


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
        wap_pickle = open('wap_pickle.txt', 'rb')
        war_and_peace = pickle.load(wap_pickle)
        start = random.randint(20*1000, 100*1000)
        a = war_and_peace[start:start+length]
    return(a)

#Use words.txt
def word_handler(text):
    foo = text.split(' ')
    bad_nums = []
    for num in range(len(foo)):
        if '\n' in foo[num]:
            foo += foo[num].split('\n\n')
            bad_nums.append(num)
            
    
    out = []
    for num in range(len(foo)):
        if not num in bad_nums:
            out.append(clean(foo[num]))

    return(out)

def dictify(word_list):
	word_dict = {}
	for word in word_list:
		try:
			word_dict[word]	+= 1
		except KeyError:
			word_dict[word] = 1
	
	return(word_dict)

            

#Use english_quadgrams.txt
class ngram_score(object):
    def __init__(self, ngram_file_name1, ngram_file_name2, sep=' '):
        """
        Generally - scorer = ngram_score('english_trigrams.txt', 'english_quadgrams.txt')
        Initializes log10 probability dictionaries self.ngrams1 & 2, as well as corresponding
        self.floors1 & 2, and self.L1 & 2 (length of ngram) . self.L1 should be of length one
        shorter than self.L2, e.g. trigram and quadgram so 3 & 4.
        """
        self.n1, self.n2 = self.initialize_ngram(ngram_file_name1, sep), self.initialize_ngram(ngram_file_name2, sep)
        self.ngrams1, self.floor1, self.L1 = self.n1[0], self.n1[1], self.n1[2]
        self.ngrams2, self.floor2, self.L2 = self.n2[0], self.n2[1], self.n2[2]
        
    def score(self,text):
        """compute the probability score of text: e.g. iloveyou, returns log10 of
        p(ilov) * p(love)/p(lov) * p(ovey)/p(ove) * p(veyo)/p(vey) * p(eyou)/p(eyo), equivalent to
        p(ilo) * p(v|ilo) * p(e|lov) * p(y|ove) * p(o|vey) * p(u|eyo), roughly equivalent to
        p(i) * p(l|i) * p(o|il) * p(v|ilo) * p(e|ilov) * p(y|ilove) * p(o|ilovey) * p(u|iloveyo)
        """
        log_score = 0
        for i in range(len(text)-self.L2+1):
            temp = text[i:i+self.L2]
            if temp in self.ngrams2:
                log_score += self.ngrams2[temp]
            else:
                log_score += self.floor2
        for i in range(1, len(text)-self.L1+1):
            temp = text[i:i+self.L1]
            if temp in self.ngrams1:
                log_score -= self.ngrams1[temp]
            else:
                log_score -= self.floor1
            
        return(log_score)

    def initialize_ngram(self, ngram_file_name, sep=' '):
        """
        Takes in the name of an ngram frequency file, returns [a, b, c] where a is the log10 probability
        Dictionary, b is the floor, log10(0.01/total_freq), and c the ngram length (3 or 4 etc.)
        """
        ngram_file = open(ngram_file_name)
        ngram_dir = {}
        lines = ngram_file.readlines()
        for line in lines:
            key,count = line.split(sep)
            key = key.lower()
            ngram_dir[key] = int(count)

        # length of ngram and length of text
        L = len(key)
        N = sum(ngram_dir.values())

        # calculate log probabilities of each ngram
        for key in ngram_dir.keys():
                ngram_dir[key] = log10(float(ngram_dir[key])/N)
        floor = log10(0.01/N)
        ngram_file.close()

        return([ngram_dir, floor, L])

    



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

        
        
