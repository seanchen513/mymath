"""
This solves LC279 Perfect Squares using number theory.

Theory:

1. Lagrange's four-square theorem: every natural number can be represented 
as the  sum of four integer squares (including 0 squares).  Ie, every positive
integer can be represented as the sum of 1, 2, 3, or 4 positive squares.

2. Legendre's three-square theorem: a natural number can be represented as the 
sum of three squares (including 0 squares) if and only if n is not of the form 
n=(4^a)(8b+7) for nonnegative integers a and b.

The first numbers that cannot be expressed as the sum of three squares
(including 0 squares) (ie, numbers that can be expressed as n=(4^a)(8b+7)) are:
7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71 ...

So, by Lagrange's theorem, these integers can be represented as the sum of
four positive squares.

So a positive integer can be represented by 3 positive squares if and only if
it is not a square itself, it is not a sum of squares, and it does not have
the form n=(4^a)(8b+7).

3. Sum of two squares theorem: an integer greater than one can be written as a 
sum of two squares (including 0 squares) if and only if its prime decomposition
contains no prime congruent to 3 mod 4 raised to an odd power.

Examples using fact that 7 = 3 mod 4, but 2 and 5 are not:
2540 = 2 * 5^2 * 7^2 = 7^2 + 49^2.
3430 = 2 * 5 * 7^3 cannot be expressed as the sum of two squares.

Following is special case:

4. Fermat's theorem on sums of two squares: an odd prime p can be expressed as
the sum of two squares if and only if p = 1 (mod 4).  Such an odd prime is
called a Pythagorean prime.

Examples: 
5 = 1 + 4
13 = 4 + 9
17 = 1 + 16
29 = 4 + 25 
37 = 1 + 36
41 = 16 + 25
"""

# Assume n >= 0
def is_square(n: int) -> bool:
    n_sqrt = int(n**0.5)
    return n_sqrt * n_sqrt == n

###############################################################################
"""
Sum of two squares theorem: an integer greater than one can be written as a 
sum of two squares (including 0 squares) if and only if its prime decomposition
contains no prime congruent to 3 mod 4 raised to an odd power.

Examples using fact that 7 = 3 mod 4, but 2 and 5 are not:
2540 = 2 * 5^2 * 7^2 = 7^2 + 49^2.
3430 = 2 * 5 * 7^3 cannot be expressed as the sum of two squares.

Consider only positive squares.  Eg, 16 = 16 + 0 is not considered
a sum of two squares here.
"""
def sum_of_two_squares(n : int) -> bool:    
    from primes import prime_factorization_dict

    if is_square(n):
        return False

    d = prime_factorization_dict(n)
    
    for prime, power in d.items():
        if (prime % 4 == 3) and (power % 2 == 1):
            return False

    return True

# This is probably faster...
def sum_of_two_squares2(n : int) -> bool:
    end = int(n**0.5) + 1

    # for i in range(1, end):
    #     if is_square(n - i*i):
    #         return True

    # return False

    return any(is_square(n - i*i) for i in range(1, end))

"""
Legendre's three-square theorem: a natural number can be represented as the 
sum of three squares (including 0 squares) if and only if n is not of the form 
n=(4^a)(8b+7) for nonnegative integers a and b.

The first numbers that cannot be expressed as the sum of three squares
(including 0 squares) (ie, numbers that can be expressed as n=(4^a)(8b+7)) are:
7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, 79, 92, 112, ...

So, by Lagrange's theorem, these integers can be represented as the sum of
four positive squares.

If legendre_form(n) == True, then n is the sum of four positive squares.
"""
def sum_of_four_squares(n: int) -> bool:
    # Assume n > 0.
    while (n & 3) == 0: # n % 4 == 0
        n >>= 2 # n //= 4

    return (n & 7) == 7 # n % 8 == 7

def sum_of_four_squares2(n: int) -> bool: # aka legendre_form()
    # Assume n > 0.
    while n % 4 == 0:
        n //= 4

    return n % 8 == 7

"""
Returns minimum number of positive squares that add up to given integer n.
"""
def num_squares(n: int) -> int:
    if is_square(n):
        return 1

    #if sum_of_two_squares(n):
    if sum_of_two_squares2(n):
        return 2

    #if sum_of_four_squares(n):
    if sum_of_four_squares2(n):
        return 4

    return 3
    #primes_cong3 = [3,7,11,19,23,31,43,47,59,67,71,79,83,91,103]
    #primes_cong1 = [5,13,17,29,37,41,53,61,73,89,97,101] # sum of two squares
    #legendre = [7,15,23,28,31,39,47,55,60,63,71,79,92,112]
    
    #if n in primes_cong1:
    #    return 2


###############################################################################

if __name__ == "__main__":
    print("="*80)

    d = {1: [], 2: [], 3: [], 4: []}

    for i in range(1000):
        n_sq = num_squares(i)
        d[n_sq].append(i)

        print(f"{i}: {n_sq}", end=", ")
    
    print("\n")   
    print("="*80)

    for n_sq, lst in d.items():
        print(f"\nSum of {n_sq} square(s):")
        print(lst)
        print()
