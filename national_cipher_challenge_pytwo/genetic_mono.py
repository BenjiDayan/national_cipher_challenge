# genetic_mono
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

english_ranking = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', \
                   'm', 'w', 'f', 'y', 'g', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z']

import random
import basics
import math

file = open('english_trigrams.txt')
quad_scorer = basics.ngram_score(file)



class node():
    def __init__(self, keyword):
        self.keyword = keyword

    def breed2(self, another):
        #some horrible method necessary to ensure a full alphabet is the result
        other_keyword = another.keyword
        baby_keyword_index = [x for x in range(len(self.keyword))]
        letters_left = alphabet.copy()
        baby_keyword = ['' for letter in self.keyword]
        for num in range(len(self.keyword)):
            bbindex = random.choice(baby_keyword_index)
            a = self.keyword[bbindex]
            b = other_keyword[bbindex]
            if a in baby_keyword and b in baby_keyword:
                char = random.choice(letters_left)
            elif a in baby_keyword:
                char = b
            elif b in baby_keyword:
                char = a
            else:
                foo = random.randint(0, 8)
                if foo in [0, 1, 2, 3]:
                    char = a
                elif foo in [4, 5, 6, 7]:
                    char = b
                else:
                    char = random.choice(letters_left)
            letters_left.remove(char)
            baby_keyword_index.remove(bbindex)
            baby_keyword[bbindex] = char

        return(node(''.join(baby_keyword)))

    def breed(self, another):
        other_keyword = another.keyword
        letters_left = alphabet.copy()
        baby_keyword = ['' for letter in self.keyword]
        for num in range(len(self.keyword)):
            i = alphabet.index(english_ranking[num])
            a = self.keyword[i]
            b = other_keyword[i]
            if a in baby_keyword and b in baby_keyword:
                char = random.choice(letters_left)
            elif a in baby_keyword:
                char = b
            elif b in baby_keyword:
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
            baby_keyword[i] = char
        return(node(''.join(baby_keyword)))


class genetic_woo():
    def __init__(self, population_size, text):
        # num is number of nodes to have
        self.text = text
        self.breeding_times = 6 # how many times each parent will breed
        self.population_size = population_size
        self.population = [] # stores the current population
        self.past_generations = [] # stores the previous generations
        self.complete_scores = [] # stores the complete score history
        self.summary_scores = [] # stores min max mean median
        self.base_score = quad_scorer.score(basics.generate_random_text(len(text)))
        self.english_score = quad_scorer.score(basics.generate_english_text(len(text)))                                             

        self.mono = [x[0] for x in basics.freq_analysis(text, 1, 26)]
        for char in alphabet:
            if not char in self.mono:
                self.mono.append(char)
                
        for num in range(population_size):
            self.population.append(node(''.join(self.make_keyword())))

    def make_keyword(self):
        keyword = []
        # The position in the messed_up_ranking is shuffled a bit
        messed_up_ranking = english_ranking.copy()
        for num in range(1):
            for index in range(25):
                if random.randint(0, 1):
                    a = messed_up_ranking[index]
                    messed_up_ranking[index], messed_up_ranking[index+1] = \
                                              messed_up_ranking[index+1], a
        
        #This would makes the ideal letter for letter for the frequency if not for
        #The messed_up_ranking being a little messed up.
        for alphanum in range(26):
            ranking_index = messed_up_ranking.index(alphabet[alphanum])
            keyword.append(self.mono[ranking_index])
        
        return(keyword)
    
    def score(self, my_node):
        return(quad_scorer.score(self.node_to_text(my_node)))
        

    def node_to_text(self, my_node):
        return(decrypt(my_node.keyword, self.text))

    def breed(self):
        self.offspring = [] # the offspring that will be produced
        # 0 will be number of times it's been bred
        available = [[x, 0] for x in self.population] # who is left available
        while True:
            # take the first node in available as the base, breed them with random partners in
            # available, then remove first guy from available
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

    def cull(self):
        # Removes members of the population until the population fits self.population_size
        # population ranking is of the form [original index, score]
        population_ranking = [[x, self.score(self.population[x])] for x in range(len(self.population))]
        population_ranking.sort(key=lambda x: x[1]) # sort the population_ranking by score

        #population_ranking is now sorted from lowest -lots, to highest -not so much       
        #return([[self.population[x[0]] for x in population_ranking[-self.population_size:]], population_ranking])
        self.population = [self.population[x[0]] for x in population_ranking[-self.population_size:]]
        self.ranking = [x[1] for x in population_ranking[-self.population_size:]]

        #score keeping
        self.complete_scores.append(self.ranking)
        minimum = self.ranking[0]
        maximum = self.ranking[-1]
        mean = sum(self.ranking)/self.population_size
        median = self.ranking[math.ceil(self.population_size/2)]
        self.summary_scores.append([minimum, maximum, mean, median])
        
    
                


def decrypt(keyword, text):
    dtext = ''
    for char in text:
        a = keyword.index(char)
        dtext += alphabet[a]
    return(dtext)
    
        
