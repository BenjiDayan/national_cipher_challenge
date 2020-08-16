#bifid
import basics
import math
import random

#modified alphabet, has no 'j'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = 'htpegweehwaohcpnirxeiexzgogdqkuegbykhwaocdotqotslyoeldumoseqoqytprnnigabadvqiaxvoodeegwssfqrggsyegwsseqsxbtkbrftgbykbkeuqnetcksoqbfotsyqeosurbctekyormtplrattkmobkeuokcndzmrotrncoywqkpshvtcvnftqetcalwavvfukbskfhrasaqvfcrsgbtttqwnevyfrheaqchsqqtnndpbtcpzegreakkohurrocxnqgkncqstbsnqbmtzooseborxkdehehroykeobbfikqttcizccoruihgytimbahoawoozsoqrocdssoqdgeymkloaqkxobkpsfhsvlkwtehnatktouknsiocydltqgitnuocrkceposrqcqqcqsrhlwnoskennbtflolenawbocytnetrnowdeksoqipdwheawlovvyfscdotlinsosyqopynhtoconrpthnawcoodytcorethlulaeqrpbnzcsehcisdnrtndtspsqfcrbnpsysrbeuelkeqteyqqlzlyksobdkntgtwburrblqakbscvliiuvtfqbpakgstclsfscksksobaorebqevcbhqblsviqoulkothqnfoiosahratktoxquehrynbkpskqofnwseuocxsoqyovefscnreqspuoedlfwkforuingtkgoasdqsgeymkqopiodevsfncersqupesoqywbekbqkpiadcoiugnctoiivoqbtzcpenbhzkagoycqpcdetmiwfebgeueorycgsyekmoqipdaocuingthwaoqvtetvcubtoysoqybqybgltnkvtfvqtfhstqesrqdeumuknsiocyferrblsrhqsthkpetrpewbeosbqkqmpzbrueblhthhcsbdacigcyrenthrauqnenktonotwthuikhioosgqegohxirwteinsqyffqnktltrscnetrgeydanrlhfptktofdqtsoqragftlhvntsnyiivoqetsbkfyosepqivltoyehmirwheawgotboqxrhrakbrrgtxprsehflrbiflqoodegaenoouxwlelsehthmirudkqadvtihroiccqtoyehmirihwoibcrqlplwheawxobofyqevrtrgxqlbqntbyyrebtrtteenrmsdhqoqxtcloifeqthuatoouwbntsibdukhsnqvrarcthvrsecqsnsoqysfhrgutroureiovuqputtlavnvmtslxdnhoawboepgqeckeotheauotuvlclbpeqgceekqntbgeueoryebtqgelrsoqyvttyhmirvttxhqovfokrkqfenknoblelcqrrwgoeolsogeynhuatovufnhtzxdstulqfscqqghycnvscueurlkaslodtsbqrmrpetlmenhtasgstfotdhqtuniwqipokomeggfttgoexvtcmbmargeynkfosktyeobdukbsemctrqvriuitzbrydcfsoscqrliqoeaebbsrqgpecdaqvbdubgcyeqetsbkfygeynouteqttngsuqdksysgbzufkrlobgtvwiwsoqokdysgbzuckrgeyigoenkkomane'
def split_bi(text, period):
    """Splits text into bigrams by period length
    abcdefgh period four makes [ae, bg, cg, dh]"""
    comp = []
    for num in range(len(text) - period):
        comp.append(text[num] + text[num+period])

    return(comp)

def counts(bigram_list):
    """Takes a list like ['ae', 'bg', 'ae, 'sd']
    And outputs number of occurences of things so [2, 1, 1]"""
    stuff_dict = {}
    for thing in bigram_list:
        try:
            stuff_dict[thing] += 1
        except KeyError:
            stuff_dict[thing] = 1

    comp = [stuff_dict[key] for key in stuff_dict]
    comp.sort()
    return(comp)

"""Key should be of the form
col0    1    2    3    4
[['a', 'b', 'c', 'd', 'e'], 
 ['f', 'g', 'h', 'i', 'k'], 
 ['l', 'm', 'n', 'o', 'p'], 
 ['q', 'r', 's', 't', 'u'], 
 ['v', 'w', 'x', 'y', 'z']]
 . """

class bifid_node(basics.node):
    def reproduce(self, another):
        keyword = self.keyword
        other_keyword = another.keyword

        #Sometimes starts from other end of keyword to aid free movement
        switched = random.randint(0, 1)
        if switched:
            keyword, other_keyword = keyword.copy(), other_keyword.copy()
            keyword.reverse()
            other_keyword.reverse()

        baby_keyword = [[] for num in range(5)]
        letters_left = alphabet.copy()
        letters_used = []
        for row_num in range(5):
            for column_num in range(5):
                a = keyword[row_num][column_num]
                b = other_keyword[row_num][column_num]
                if a in letters_used and b in letters_used:
                    char = random.choice(letters_left)
                elif a in letters_used:
                    char = b
                elif b in letters_used:
                    char = a
                else:
                    if random.randint(0, 1):
                        char = a
                    else:
                        char = b

                #Occasionally do mutation
                if random.randint(0, 16) == 16:
                    char = random.choice(letters_left)

                #print(letters_left)

                baby_keyword[row_num].append(char)
                letters_left.remove(char)
                letters_used.append(char)

        if switched:
            baby_keyword.reverse()

        return(bifid_node(baby_keyword))
                    
                

class bifid_solver(basics.genetic_algorithm):
    def __init__(self, text, population_size, breeding_times, decrypt_function, node_class, period):
        super(type(self), self).__init__(text, population_size, breeding_times, decrypt_function, node_class)
        self.period = period
        self.initialize_population()

    def score(self, my_node):
        return(self.scorer.score(self.decrypt_function(self.text, my_node.keyword, self.period)))

    def make_keyword(self):
        #Makes a random keyword
        keyword = [[] for num in range(5)]
        letters_left = alphabet.copy()
        for row_num in range(5):
            for column_num in range(5):
                keyword[row_num].append(random.choice(letters_left))

        return(keyword)

    def initialize_population(self):
        for num in range(self.population_size):
            self.population.append(self.node(self.make_keyword()))
        


def decrypt(text, key, period):
    num_pair_list = []
    for char in text:
        num_pair_list.append(char2num(char, key))

    #print(num_pair_list)

    periodicized_pair_list = periodicize(num_pair_list, period)
    #print(periodicized_pair_list)

    switched_up_still_periodicized_pair_list = switch_up(periodicized_pair_list, period)

    output = ''
    for periodthing in switched_up_still_periodicized_pair_list:
        for numpair in periodthing:
            output += num2char(numpair, key)

    return(output)


def switch_up(periodicized_pair_list, period):
    """Repairs the numbers. if the first period is ['32', '32', '23', '12', '15']
    It will turn it into ['33', '21', '32', '21', '25'].
    Note the last period might be shorter, so deals with that separately
    """
    #Leaves last period for last
    comp = []
    for num in range(len(periodicized_pair_list) - 1):
        string = ''.join(periodicized_pair_list[num])
        output = []
        for num in range(period):
            output.append(string[num] + string[num+period])
        comp.append(output)

    length_last_period = len(periodicized_pair_list[-1])
    string = ''.join(periodicized_pair_list[-1])
    output = []
    for num in range(length_last_period):
        output.append(string[num] + string[num+length_last_period])

    comp.append(output)
    return(comp)
        
        


def periodicize(num_pair_list, period):
    """Returns a list
    num_pair_list = [[3,2], [3,2],231215 3512234211 2455224412 2233544124 1242421224 522441]
    period=5
    should take the first ten, match 1 with 5, 2 with 6, 3 with 7 and so on
    """
    #Divided up into the first period of pairs, second period
    #so [ [[], [], [], [], []] , [ [], [], [], [], []] ...
    length = len(num_pair_list)
    periodicized_pair_list = []
    limit = math.floor(length/period)
    for num in range(limit):
        periodicized_pair_list.append(num_pair_list[period*num:period*(num+1)])

    #If there's extra stuff on the end,
    if not limit == length/period:
        periodicized_pair_list.append(num_pair_list[period*limit:])

    return(periodicized_pair_list)


def num2char(numpair, key):
    """Takes in a numpair like '34', and returns the character in row 3 (actually 4th row)
    and column 4 (actually 5th column) of the key"""
    row_num = int(numpair[0])
    column_num = int(numpair[1])
    return(key[row_num][column_num])

def char2num(char, key):
    """Returns the number, 'row_numcolumn_num', of the char in the key
    if row=4, column=2, returns '42'"""
    row_num = 0
    column_num = 0
    for num in range(5):
        if char in key[num]:
            row_num = num
            column_num = key[num].index(char)
            break

    return(str(row_num) + str(column_num))
    


