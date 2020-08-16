import basics
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import cProfile
import pstats
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
        self.cycles_count = 0

        self.graphing = False #When turned on, cull() passes new scores to the graph

        #self.initialize_population()

    def initialize_graph(self):
        self.graphing = True
        self.ax = plt.gca()

        if len(self.summary_scores) > 0:
            start_num_points = len(self.summary_scores)
            xdata = np.array([x for x in range(1, start_num_points)])
            self.lines = [self.ax.plot(xdata, [score[num] for score in self.summary_scores])[0]  for num in range(3)]
        else:
            self.lines = [self.ax.plot([], [])[0] for num in range(3)]

        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        plt.ion()
        plt.show()

    def update_line(self, line, new_data):
        #Given a line and new_data of the form [new_x, new_y], adds on the new values
        line.set_xdata(np.append(line.get_xdata(), new_data[0]))
        line.set_ydata(np.append(line.get_ydata(), new_data[1]))

    def update_graph(self):
        for num in range(len(self.lines)):
            self.update_line(self.lines[num], [self.cycles_count, self.summary_scores[-1][num]])
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        plt.draw()
        plt.pause(0.01)

        
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
            self.cycles_count += 1
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
        if self.graphing == True:
           self.update_graph()
                
                
                
            

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


def algorithm_avg_time(n, score, algorithm, *args, graphing=False, **kwargs):
    """Makes n algorithms, returns the avg time for them to run to a score, given"""
    algorithms = []
    for num in range(n):
        algorithms.append(algorithm(*args, **kwargs))
        if graphing:
            algorithms[-1].initialize_graph()

    prof = cProfile.Profile()
    for num in range(n):
        print('{0} out of {1}:'.format(num+1, n), end='')
        prof.runctx('algorithms[num].run_to_score(score)', globals(), locals())
        
        if graphing:
            for line in algorithms[num].lines:
                line.remove()
    stats = pstats.Stats()
    stats.add(prof)
    return(stats)
    
