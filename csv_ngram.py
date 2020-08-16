#csvngram dealer

import csv
import math

class probber():
    def __init__(self, csvfilename1, csvfilename2):
        """Takes in the file names of the e.g. ngrams3.csv and ngrams4.csv
        Sets up logprob_list1 & 2"""
        
        self.csvfile1 = open(csvfilename1, newline='')
        self.csvfile2 = open(csvfilename2, newline='')

        self.csvreader1 = csv.reader(self.csvfile1, delimiter=',')
        self.csvreader2 = csv.reader(self.csvfile2, delimiter=',')

        self.logprob_list1 = self.make_logprob_list(self.csvreader1)
        self.logprob_list2 = self.make_logprob_list(self.csvreader2)

        self.logprob_dir1 = {}
        self.logprob_dir2 = {}
        for thing in self.logprob_list1:
            self.logprob_dir1[thing[0]] = thing[1]
        for thing in self.logprob_list2:
            self.logprob_dir2[thing[0]] = thing[1]

        self.csvfile1.close()
        self.csvfile2.close()

    def make_logprob_list(self, csvreader):
        #Given a csvreader of an ngramsX.csv, returns a logprob_list
        logprob_list = []
        for row in csvreader:
            logprob_list.append(row)

        del(logprob_list[0])
        comp = 0
        for num in range(len(logprob_list)):
            logprob_list[num] = [logprob_list[num][0], int(logprob_list[num][1])]
            comp += logprob_list[num][1]

        #Aka turns all the ngram counts into ln(counts/totalcounts), or ln(prob)
        complog = math.log(comp)
        for num in range(len(logprob_list)):
            logprob_list[num][1] = math.log(logprob_list[num][1]) - complog

        return(logprob_list)
        
"""
logprob_list4 = []

for row in csvreader4:
    logprob_list4.append(row)

del(logprob_list4[0])

comp4 = 0
for num in range(len(logprob_list4)):
    logprob_list4[num] = [logprob_list4[num][0], int(logprob_list4[num][1])]
    comp4 += logprob_list4[num][1]

comp4log = math.log(comp4)
for num in range(len(logprob_list4)):
    a = math.log(logprob_list4[num][1]) - comp4log
    newprob_list.append([logprob_list[num][0], math.log(logprob_list[num][1]/comp)])
    logprob_list[num][1] = a
"""
