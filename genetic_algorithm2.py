import basics
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import time

class node():
    # Has a keyword that defines it's means ofo decrypting the text
    # Can reproduce to make a mutated offspring
    def __init__(self, key=None):
        self.key = key

    def reproduce(self):
        pass

class algorithm():
    #has a population of nodes with keywords, can breed to make offspring with random
    #mutations/changes, can cull to select for best english scoring offspring
    
    def __init__(self, text, population_size, breeding_times, node_class):
        self.text = text
        self.breeding_times = breeding_times # how many times each parent will breed
        self.population_size = population_size
        self.population = []
        self.past_generations = []
        self.complete_scores = [] # stores the complete score history
        self.summary_scores = [] # stores min max mean median
        self.node = node_class # stores the type of node

        self.scorer = basics.ngram_score('english_trigrams.txt', 'english_quadgrams.txt')
        self.base_score = self.scorer.score(basics.generate_random_text(len(text)))
        self.english_score = self.scorer.score(basics.generate_english_text(len(text)))

        self.graphing = False #When turned on, cull() passes new scores to the graph

        #self.initialize_population()

    def initialize_graphing(self, chunk_size):
        self.graphing = True
        self.fig = plt.figure()
        self.axes = [self.fig.add_subplot(111)]

        #Chunks of chunk_size number of cycles are displayed together. Make sure we have enough space?
        self.number_of_cycles = len(self.summary_scores)
        self.chunk_size = chunk_size #How many cycles to be displayed in each chunk
        num_left = self.number_of_cycles
        count = 0
        self.xdata = [] #list of xdatas
        self.lines = [] #list of lines
        while num_left > 0:
            self.xdata.append(np.arange(self.chunk_size))
            ydata = self.summary_scores[count*self.chunk_size:(count+1)*self.chunk_size]
            print(ydata)
            self.lines.append(plt.plot(self.xdata[-1], ydata)[0])
            num_left -= self.chunk_size
            count += 1
        #Cap off the ydata of the last set which may not be complete
        self.lines[-1].set_ydata(ydata + (self.chunk_size - len(ydata))*([self.base_score]*3))                             

        
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        self.fig.canvas.draw()
        plt.ion()
        plt.show(block=False)
        

    def initialize_population(self):
        # Initializes the population with size self.population, hopefully near to endpoint
        pass

    def score(self, my_node):
        return(self.scorer.score(self.decrypt(self.text, my_node.key)))

    def decrypt(self, text, key):
        pass

    def cycle(self, ntimes=1):
        # Does ntimes cycles of breed and cull
        for num in range(ntimes):
            self.breed()
            self.cull()

    def run_to_score(self, score):
        # Keeps cycling until the latest population's mean score is greater than score
        while True:
            self.cycle()
            if self.summary_scores[-1][2] > score:
                break

    def turnover(self, breeding_times, num_cycles_small, num_cycles_large, cullsize):
        for num in range(num_cycles_large):
            for num in range(num_cycles_small):
                self.breed(size=len(self.population), times=breeding_times)
            self.cull(size=cullsize)
        
        

    def breed(self, size=None, times=None):
        """Replaces self.population with a whole load of newly bred offspring, randomly
        selecting who pairs with who"""
        if size == None:
            size = self.population_size
        if times == None:
            times = self.breeding_times
        
        self.offspring = []
        for pop_num in range(size):
            for breed_num in range(times):
                self.offspring.append(self.population[pop_num].reproduce())

        # archive the parent generation, make the new population the offspring.
        self.past_generations.append(self.population)
        self.population = self.offspring

    def cull(self, size=None):
        #size is the final size (post culling) of the population
        if size == None:
            size = self.population_size
        """Removes the bottom scorers of the population until the population fits
        population_size"""

        # From each node in population we get [node_index, node_score] in population_ranking
        population_ranking = [[x, self.score(self.population[x])] for x in \
                              range(len(self.population))]
        population_ranking.sort(key=lambda x: x[1]) # sort by score from lowest to highest

        # The new population is the top population_size guys as ranked
        # x[0] is the index of the node
        self.population = [self.population[x[0]] for x in population_ranking[-size:]]
        # The actual scores, with the same indices as their node counterparts in population
        self.ranking = [x[1] for x in population_ranking[-size:]]

        #score keeping
        self.complete_scores.append(self.ranking)
        botpercentile = self.ranking[math.floor(0.05*size)]
        toppercentile = self.ranking[math.floor(0.95*size)]
        median = self.ranking[math.ceil(size/2)]
        self.summary_scores.append([botpercentile, median, toppercentile])

        # if graphing is turned on, send the new data to the graph
        #if self.graphing == True:
           # self.number_of_cycles += 1
           # if self.number_of_cycles % self.chunk_size == 0: #We're filled up, start a new plot
                
                
                
            

class genetic_algorithm(algorithm):
    
    def breed(self, size=None, times=None):
        """Replaces self.population with a whole load of newly bred offspring, randomly
        selecting who pairs with who"""

        if size == None:
            size = self.population_size
        if times == None:
            times = self.breeding_times

            
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
                self.offspring.append(available[0][0].reproduce(choice[0]))
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


def algorithm_avg_time(n, score, algorithm, *args, **kwargs):
    """Makes n algorithms, returns the avg time for them to run to a score, given"""
    algorithms = []
    for num in range(n):
        algorithms.append(algorithm(*args, **kwargs))

    prof = cProfile.Profile()
    for num in range(n):
        prof.runctx('algorithms[num].run_to_score(score)', globals(), locals())
    stats = pstats.Stats()
    stats.add(prof)
    return(stats)
    
