import math

def prime4u():
    '''Returns a prime number'''
    return(3)

def highest_common_factor(numbers):
    '''Takes in "numbers", a list of numbers to find the highest common factor of '''
    prime_factors = []
    primes = []
    for number in numbers:
        prime_factors.append(prime_factorize(number))

    shared = {}
    for pfs in prime_factors:
        for p in pfs:
            try:
                if shared[p[0]] > p[1]:
                    shared[p[0]] = p[1]
            except KeyError:
                shared[p[0]] = p[1]


    is_prime_in_shared = 0
    for number in prime_factors:
        for prime in number:
            is_prime_in_shared = 0
            for prime_key in shared:
                if prime_key == prime[0]:
                    is_prime_in_shared = 1
            
            if is_prime_in_shared == 0:
                del(shared[prime[0]])

    print(prime_factors)
    return(shared)
    

    
        

    
    
    

def prime_factorize(integer):
    '''Returns the prime factors of "integer", in the form of a list of lists,
    each containing first the prime factor, and second to the power of what
    '''
    if integer == 1:
        return([])
    
    prime_factors = []
    primes = find_primes(integer)

    for prime in primes:
        to_the_power_of = 1
        while integer % prime**to_the_power_of == 0:
            to_the_power_of += 1

        if not to_the_power_of - 1 == 0:
            prime_factors.append([prime, to_the_power_of - 1])

    return(prime_factors)


def is_prime(x):
    ''' if x is prime, returns True, else returns False. Only accepts integers'''


          
    for number in range (2, int(math.sqrt(x)) + 1):
        if x % number == 0:
            return(False)

    if x == 1:
        return(False)
    return(True)
    

def find_primes(limit):
    '''Returns a list of all the prime numbers from 1 to limit inclusive'''
    primes = []

    if limit > 2:
        primes.append(2)
# note int(1.5) returns 1
    for number in range(3,limit + 1, 2):
        if is_prime(number):
            primes.append(number)        
    return(primes)

def count(iterable):
    '''Returns number of iteration thingys in iterable'''
    count = 0
    for thing in iterable:
        count += 1
    return(count)
