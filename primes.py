"""
"""

from typing import List
#import math


def divisors(n):
    pass

################################################################################
"""
Returns list of all prime factors (repeated) of given integer n.
They are sorted.

Example: 720 = 2^4 * 3^2 * 5

prime_factors(720) returns [2,2,2,2,3,3,5]
"""
def prime_factors(n: int) -> List: # aka prime divisors
    if n <= 1:
        return []

    p_div = []

    while n % 2 == 0:
        p_div.append(2)
        n //= 2

    # n now odd
    end = int(n**0.5) + 1
    for i in range(3, end, 2):
        while n % i == 0:
            p_div.append(i)
            n /= i

    # if n is still > 2, it must be a prime itself
    if n > 2:
        p_div.append(int(n))
    
    return p_div

"""
Returns prime factorization of given integer n as a dict mapping
prime factors to their positive integer powers.

Example: 720 = 2^4 * 3^2 * 5

prime_factorization_dict(720) returns dict:
{
    2: 4,
    3: 2,
    5: 1
}
"""
def prime_factorization_dict(n: int) -> dict:
    from collections import defaultdict

    if n <= 1:
        return None

    p_div = defaultdict(int)

    while n % 2 == 0:
        p_div[2] += 1
        n //= 2

    # n now odd
    end = int(n**0.5) + 1
    for i in range(3, end, 2):
        while n % i == 0:
            p_div[i] += 1
            n /= i

    # if n is still > 2, it must be a prime itself
    if n > 2:
        p_div[int(n)] = 1
    
    return p_div

"""
Returns prime factorization of a given integer n as a list of tuples
(prime factor, positive integer power).

Example: 720 = 2^4 * 3^2 * 5

prime_factorization(720) returns dict:
[(2,4), (3,2), (5,1)]
"""
def prime_factorization(n: int) -> List[tuple]:
    d = prime_factorization_dict(n)

    return [(p, power) for p, power in d.items()] if d else None

################################################################################
"""
Primality test: returns whether given integer n is a prime.

Every prime > 3 has form 6k-1 or 6k+1.

Forms 6k, 6k+2, and 6k+4 are even, so can't be prime unless 2.
Form 6k+3 is divisible by 3, so can't be prime unless 3.
That leaves forms 6k+1 and 6k-1 (ie, 6k+5).
"""
def is_prime(n: int) -> bool:
    if n < 2:
        return None

    if n == 2 or n == 3:
        return True

    if (n % 2 == 0) or (n % 3 == 0):
        return False

    d = 5 # possible divisors to check
    n_sqrt = int(n**0.5) + 1

    while d <= n_sqrt:
        # might do an extraneous comparison for d+2 > n_sqrt
        if (n % d == 0) or (n % (d+2) == 0):
            return False
            
        d += 6        

    return True

###############################################################################
"""
Finds all primes up to and including given integer n.

Only keep table of odd integers >= 3 to save space.
For table, use dict mapping (odd integer >= 3) -> boolean representing
whether k is prime.  Boolean initialized to True.

https://www.quora.com/Can-you-write-a-C-program-that-finds-all-prime-numbers-from-2-to-2-billion-in-under-1-second-on-an-average-500-PC

"""
def sieve_of_eratosthenes(n: int) -> List:
    end = int(n**0.5) + 1

    sieve = {k: True for k in range(3, n+1, 2)}

    for i in range(3, end, 2):
        if sieve[i]:
            # Suffices to start at i*i since smaller multiples of i were
            # already crossed out in a previous iteration of i.
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
"""
Korselt's criterion
Theorem (A. Korselt 1899): A positive composite integer n is a Carmichael number
if and only if n is square-free, and for all prime divisors p of n, 
it is true that (p - 1) | (n - 1).

Smallest Carmichael number is 561 = 3*11*17.
2 | 560, 10 | 560, 16 | 560

Next smallest Carmichael numbers: 1105, 1729, 2465, 2821, 6601, 8911
"""
def is_carmichael(n : int) -> bool:
    p_divisors = prime_factors(n)

    # Carmichael numbers have at least 3 distinct prime factors
    if len(p_divisors) <= 2: 
        return False

    # n can only be square-free if no prime divisors are repeated
    if len(p_divisors) != len(set(p_divisors)): 
        return False

    # Now check (p - 1) | (n - 1) for all prime divisors of n
    n_dec = n - 1
    for p in p_divisors:
        if n_dec % (p - 1) != 0:
            return False

    return True

################################################################################

if __name__ == "__main__":
    def test_primality(n=100):
        print(f"\nChecking for prime numbers up to {n}:")

        for i in range(1, n+1):
            if is_prime(i):
                print(i, end=", ")

        print()

    def test_carmichael():
        print("\nChecking for Carmichael numbers up to 100,000:\n")

        for n in range(1, 100001):
            if is_carmichael(n):
                print(n)

    def test_prime_factors(n):
        from functools import reduce

        p_div = prime_factors(n)
        print("\nPrime factors of {}: {}".format(n, p_div))

        if p_div:
            product = reduce(lambda x, y: x*y, p_div)
            print("Verifying product of prime factors is: {}\n".format(product))

    def test_prime_factorization(n):
        lst = prime_factors(n) # list of repeated prime factors
        tuples = prime_factorization(n) # list of tuples (prime, power)
        d = prime_factorization_dict(n) # dict primes -> powers
        
        print("="*80)
        print(f"integer = {n}")
        print("\nList of repeated prime factors:")
        print(lst)

        print("\nList of tuples (prime, power):")
        print(tuples)

        print("\nDict of primes -> powers:")
        print(d)
        print()

    def test_prime_factorization_arr(arr):
        print("="*80)
        print("Test of prime factorizations in different formats:")
        print("1. List of repeated prime factors")
        print("2. List of tuples (prime, power)")
        print("3. Dict of primes -> powers\n")
        
        for n in arr:
            lst = prime_factors(n) # list of repeated prime factors
            tuples = prime_factorization(n) # list of tuples (prime, power)
            d = prime_factorization_dict(n) # dict primes -> powers

            print(n)
            print(lst)
            print(tuples)
            print(d)
            print()

    def test_sieve(n=1000):
        sieve = sieve_of_eratosthenes(n)
        print(f"\nSieve of Eratosthenes up to n = {n}:\n")
        print(sieve)

    ###

    #test_primality(1000)
    
    #test_carmichael()
    
    arr = {1, 2, 720, 1001, 2**31, 2*3*5*7*11*13*17*19*23*29*31, 600851475143}
    for n in arr:
        test_prime_factors(n)    


    #test_prime_factorization(720)
    #test_prime_factorization(1001)
    #test_prime_factorization_arr(arr)

    #test_sieve(1000)
