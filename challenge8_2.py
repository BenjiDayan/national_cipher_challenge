#challenge 8
import pickle
import basics
import math

def freq_an_nums(numlist):
    stuff = {}
    for num in numlist:
        try:
            stuff[num] += 1
        except KeyError:
            stuff[num] = 1
    return(stuff)

file = open('text.txt', 'rb')
text = pickle.load(file)
file.close()

split_text = text.split('2')[:-1]
#5920, split into 5s
chunks = []
for num in range(int(5920/5)):
    chunks.append(split_text[5*num:5*(num+1)])


#5325 multiples of 5
comp2 = []
for chunk in chunks:
    for num in range(len(chunk[0])):
        for thing in chunk:
            comp2.append(thing[num])

comp3 = []
for num in range(5325):
    comp3.append(''.join(comp2[5*num:5*(num+1)]))

alphabetized = ''
goo = {}
foo = freq_an_nums(comp3)
count = 0
for thing in foo:
    goo[thing] = basics.alphabet[count]
    count += 1

for thing in comp3:
    alphabetized += goo[thing]




           
