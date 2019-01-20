



import math


def gcd(x, y):
    pass

def lcm(x, y):
    pass


def divisors(n):
    pass


def prime_divisors(n):
    pass

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


# Korselt's criterion
# Theorem (A. Korselt 1899): A positive composite integer n is a Carmichael number if and only if 
# n is square-free, and for all prime divisors p of n, it is true that (p - 1) | (n - 1).
#
# Smallest Carmichael number is 561 = 3*11*17.
# 2 | 560, 10 | 560, 16 | 560
#
#
def carmichael(n):
    n_dec = n - 1
    pd = prime_divisors(n)

    #if any prime divisors are repeated:
    #    return False

    for p in pd:
        if n_dec % (p - 1) != 0:
            return False

    return True



for n in range(1, 101, 2):
    print("n = {} {}".format(n, is_prime(n)))







