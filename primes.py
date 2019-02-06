

import math
from functools import reduce
import pprint


def divisors(n):
    pass


def prime_divisors(n):
    p_div = []

    while n % 2 == 0:
        p_div.append(2)
        n /= 2

    # n now odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            p_div.append(i)
            n /= i

    # if n is still > 2, it must be a prime itself
    if n > 2:
        p_div.append(n)
    
    return p_div

################################################################################
# Every prime > 3 has form 6k-1 or 6k+1
def is_prime(n):
    if n < 2:
        return None

    if n == 2 or n == 3:
        return True

    if (n % 2 == 0) or (n % 3 == 0):
        return False

    d = 5
    n_sqrt = int(math.sqrt(n)) + 1

    while d <= n_sqrt:
        # might do an extraneous comparison for d+2 > n_sqrt
        if (n % d == 0) or (n % (d+2) == 0):
            return False
            
        d += 6        

    return True

################################################################################
# Only keep table of odd integers to save space
# https://www.quora.com/Can-you-write-a-C-program-that-finds-all-prime-numbers-from-2-to-2-billion-in-under-1-second-on-an-average-500-PC
def sieve_of_eratosthenes(n):
    last = int(math.sqrt(n)) + 1
    sieve = {k: True for k in range(3, n+1, 2)}

    for i in range(3, last, 2):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False

    return [2] + [k for k in range(3, n+1, 2) if sieve[k]]



"""
https://stackoverflow.com/questions/15347174/python-finding-prime-factors

if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]

"""

################################################################################
# Korselt's criterion
# Theorem (A. Korselt 1899): A positive composite integer n is a Carmichael number if and only if 
# n is square-free, and for all prime divisors p of n, it is true that (p - 1) | (n - 1).
#
# Smallest Carmichael number is 561 = 3*11*17.
# 2 | 560, 10 | 560, 16 | 560
#
# Next smallest Carmichael numbers: 1105, 1729, 2465, 2821, 6601, 8911
#
def is_carmichael(n):
    n_dec = n - 1
    p_divisors = prime_divisors(n)

    # Carmichael numbers have at least 3 distnict prime factors
    if len(p_divisors) <= 2: 
        return False

    # n can only be square-free if no prime divisors are repeated
    if len(p_divisors) != len(set(p_divisors)): # is there easier way?
        return False

    for p in p_divisors:
        if n_dec % (p - 1) != 0:
            return False

    return True


################################################################################

print("\nChecking for prime numbers up to 100:")
for n in range(1, 101):
    if is_prime(n):
        print(n)

print("\nChecking for Carmichael numbers up to 100,000:")
for n in range(1, 100001):
    if is_carmichael(n):
        print(n)

n = 600851475143
p_div = prime_divisors(n)
print("\nPrime factors of {}: {}".format(n, p_div))

product = reduce(lambda x, y: x*y, p_div)
print("Verifying product of prime factors is: {}".format(product))

sieve = sieve_of_eratosthenes(1000)
print("Sieve of Eratosthenes up to n = 1000:")
#pprint.pprint(sieve)
print(sieve)




