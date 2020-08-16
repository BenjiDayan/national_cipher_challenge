#challenge82
import pickle
import basics

file = open('gold.txt', 'rb')
mylist = pickle.load(file)
file.close()

def freq_an_nums(numlist):
    stuff = {}
    for num in numlist:
        try:
            stuff[num] += 1
        except KeyError:
            stuff[num] = 1
    return(stuff)

file = open('gold2.txt', 'rb')
gold = pickle.load(file)
file.close()

