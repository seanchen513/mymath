"""
Primes!
"""

from typing import List
#import math
import collections
import itertools

################################################################################
"""
NOT DONE
"""
def divisors(n):
	pass

###############################################################################
"""
Returns sorted list of all prime factors (repeated) of given integer n.

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
			n //= i

	# if n is still > 2, it must be a prime itself
	if n > 2:
		p_div.append(n)
	
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
	if n <= 1:
		return None

	p_div = collections.defaultdict(int)

	while n % 2 == 0:
		p_div[2] += 1
		n //= 2

	# n now odd
	end = int(n**0.5) + 1
	for i in range(3, end, 2):
		while n % i == 0:
			p_div[i] += 1
			n //= i

	# if n is still > 2, it must be a prime itself
	if n > 2:
		p_div[n] = 1
	
	return p_div

"""
Returns prime factorization of a given integer n as a sorted list of tuples
(prime factor, positive integer power).

Example: 720 = 2^4 * 3^2 * 5

prime_factorization(720) returns dict:
[(2,4), (3,2), (5,1)]
"""
def prime_factorization(n: int) -> List[tuple]:
	d = prime_factorization_dict(n)

	return [(p, power) for p, power in d.items()] if d else None

###############################################################################
"""
Primality test: returns whether given integer n is a prime.
Naive: check divisibility by integers from 2 to ~sqrt(n).
"""
def is_prime(n: int) -> bool:
	if n < 2:
		return False

	end = int(n**0.5) + 1

	# for i in range(2, end):
	#     if n % i == 0:
	#         return False
	
	# return True

	return all(n % i for i in range(2, end))

"""
Primality test: returns whether given integer n is a prime.
Checks divisibility of n by 2 and by odd integers starting with 3.
"""
def is_prime2(n: int) -> bool:
	if n == 2: 
		return True

	if n < 2 or n % 2 == 0: 
		return False

	# n is now an odd integer >= 3

	end = int(n**0.5) + 1

	# for i in range(3, end, 2):
	#     if n % i == 0:
	#         return False
	
	# return True
	
	return all(n % i for i in range(3, end, 2))

"""
Primality test: returns whether given integer n is a prime.

Uses fact: Every prime > 3 has form 6k-1 or 6k+1.

Forms 6k, 6k+2, and 6k+4 are even, so can't be prime unless 2.
Form 6k+3 is divisible by 3, so can't be prime unless 3.
That leaves forms 6k+1 and 6k-1 (ie, 6k+5).
"""
def is_prime3(n: int) -> bool:
	if n < 2:
		return False

	if n == 2 or n == 3:
		return True

	if (n % 2 == 0) or (n % 3 == 0):
		return False

	end = int(n**0.5) + 1

	# for i in range(5, end, 6):
	#     # might do an extraneous comparison for d+2 > n_sqrt
	#     if (n % i == 0) or (n % (i+2) == 0):
	#         return False

	# return True

	return all(n % i and n % (i+2) for i in range(5, end, 6))

"""
Primality test: returns whether given integer n is prime.

All primes > 5 have form 30k+i for i in (1,7,11,13,17,19,23,29).

Forms 30k+i for even i are even, so can't be prime unless 2.
Forms 30k+i for i%3==0 are multiples of 3, so can't be prime unless 3.
Forms 30k+i for i%5==0 are multiples of 5, so can't be prime unless 5.
"""
def is_prime4(n: int) -> bool:
	if n < 2:
		return False

	if n in (2,3,5):
		return True

	if (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0):
		return False

	end = int(n**0.5) + 1

	for d in range(7, end, 30):
		# might do some extraneous comparisons for d+k > n_sqrt
		if ((n % d == 0) or (n % (d+4) == 0) or (n % (d+6) == 0) or 
			(n % (d+10) == 0) or (n % (d+12) == 0) or (n % (d+16) == 0) or
			(n % (d+22) == 0) or (n % (d+24) == 0)):
			return False

	return True
	
	# coprimes = (7,11,13,17,19,23,29,31)
	# return all(n % (d+k) for d in range(0, end, 30) for k in coprimes)

"""
Primality test: returns whether given integer n is prime.

All primes > 7 have form 210k + d for d in this list of 48 integers:
(1,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
101,103,107,109,113,121,127,131,137,139,143,149,151,157,163,167,169,
173,179,181,187,191,193,197,199,209).
"""
def is_prime5(n: int) -> bool:
	if n < 2:
		return False

	if n in (2,3,5,7):
		return True

	if (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0) or (n % 7 == 0):
		return False
	
	end = int(n**0.5) + 1
	
	#coprimes = (11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,
	#	83,89,97,101,103,107,109,113,121,127,131,137,139,143,149,151,157,
	#	163,167,169,173,179,181,187,191,193,197,199,209,211)
	#return all(n % (d+k) for d in range(0, end, 210) for k in coprimes)
	
	###

	# if any(n % k == 0 for k in coprimes):
	#     return False
	# for d in range(210, end, 210):
	#     # for k in coprimes:
	#     #     if n % (d + k) == 0:
	#     #         return False
	#     if any(n % (d+k) == 0 for k in coprimes):
	#         return False

	# return True

	###

	for d in range(11, end, 210):
		# might do some extraneous comparisons for d+k > n_sqrt
		if ((n % d == 0) or (n % (d+2) == 0) or (n % (d+6) == 0) or  # 11,13,17
			(n % (d+8) == 0) or (n % (d+12) == 0) or (n % (d+18) == 0) or # 19,23,29
			(n % (d+20) == 0) or (n % (d+26) == 0) or (n % (d+30) == 0) or # 31,37,41
			(n % (d+32) == 0) or (n % (d+36) == 0) or (n % (d+42) == 0) or # 43,47,53
			(n % (d+48) == 0) or (n % (d+50) == 0) or (n % (d+56) == 0) or # 59,61,67
			(n % (d+60) == 0) or (n % (d+62) == 0) or (n % (d+68) == 0) or # 71,73,79
			(n % (d+72) == 0) or (n % (d+78) == 0) or (n % (d+86) == 0) or # 83,89,97
			(n % (d+90) == 0) or (n % (d+92) == 0) or (n % (d+96) == 0) or # 101,103,107
			(n % (d+98) == 0) or (n % (d+102) == 0) or (n % (d+110) == 0) or # 109,113,121
			(n % (d+116) == 0) or (n % (d+120) == 0) or (n % (d+126) == 0) or # 127,131,137
			(n % (d+128) == 0) or (n % (d+132) == 0) or (n % (d+138) == 0) or # 139,143,149
			(n % (d+140) == 0) or (n % (d+146) == 0) or (n % (d+152) == 0) or # 151,157,163
			(n % (d+156) == 0) or (n % (d+158) == 0) or (n % (d+162) == 0) or # 167,169,173
			(n % (d+168) == 0) or (n % (d+170) == 0) or (n % (d+176) == 0) or # 179,181,187
			(n % (d+180) == 0) or (n % (d+182) == 0) or (n % (d+186) == 0) or # 191,193,197
			(n % (d+188) == 0) or (n % (d+198) == 0) or (n % (d+200) == 0)):  # 199,209,211
			return False

	return True

###############################################################################
"""
Returns sorted list of primes up to n (inclusive).
Uses Sieve of Eratosthenes.

Use list copying via slicing in order to zero out many multiples at once. 
This is a lot faster.
"""
def primes(n: int) -> List[int]:
	if n < 2: 
		return []
	if n == 2:
		return [2]

	end = int(n**0.5) + 1
	sieve = [1]*(n+1) # use 0 and 1 as Booleans to indicate primality

	### Zero out multiples of 2 starting with 4.
	#sieve[4: n+1: 2] = [0] * len(sieve[4: n+1: 2])
	sieve[4: n+1: 2] = [0] * len(range(4,n+1,2)) # faster
	#sieve[4: n+1: 2] = [0] * ((n-4)//2 + 1) # also fast

	for i in range(3, end):
		if sieve[i]:
			#sieve[i*i: n+1: 2*i] = [0] * len(sieve[i*i: n+1: 2*i])
			sieve[i*i: n+1: 2*i] = [0] * len(range(i*i, n+1, 2*i)) # faster
			#sieve[i*i: n+1: 2*i] = [0] * ((n-i*i)//(2*i) + 1) # also fast

	return [2] + [k for k in range(3, n+1, 2) if sieve[k]]

"""
Returns sorted list of primes up to n (inclusive).
Uses Sieve of Eratosthenes.

Initialize "sieve" set to store potential primes.
Start with all nonnegative integers from 0 to n.
"""
def primes2(n: int) -> List[int]:
	if n < 2: 
		return []
	if n == 2:
		return [2]

	end = int(n**0.5) + 1
	sieve = [1]*(n+1) # use 0 and 1 as Booleans to indicate primality

	for i in range(2, end):
		if sieve[i]:
			for j in range(i*i, n+1, i):
				sieve[j] = 0

	return [2] + [k for k in range(3, n+1, 2) if sieve[k]]

"""
Returns sorted list of primes up to n (inclusive).
Uses Sieve of Eratosthenes.

Initialize "sieve" set to store potential primes.
Start with odd integers >= 3 to save space.
Sieve size is 1/2 = 50% of original.

This is essentially doing some precalculations to save space and time.

https://www.quora.com/Can-you-write-a-C-program-that-finds-all-prime-numbers-from-2-to-2-billion-in-under-1-second-on-an-average-500-PC

"""
def primes3(n: int) -> List[int]:
	if n < 2: 
		return []
	if n == 2:
		return [2]

	end = int(n**0.5) + 1
	sieve = set(range(3, n+1, 2)) # odd ints >= 3

	for i in range(3, end, 2):
		# If i was already eliminated in a previous pass, than so were
		# all it's multiples.  So no need to deal with i.
		# We increment by 2*i since i is odd and i*i is odd.
		# So i*i + i would be even, while i*i + 2i would be odd.
		# We only want to consider odd integers.

		if i in sieve:
			# Suffices to start at i*i since smaller multiples of i were
			# already crossed out in a previous iteration of i.
			# We increment by 2*i since i is odd and i*i is odd.
			# So i*i + i would be even, while i*i + 2i would be odd.
			# We only want to consider odd integers.
			for j in range(i*i, n+1, 2*i):
				sieve.discard(j)

	#return [2] + [k for k in range(3, n+1, 2) if k in sieve] # sorted
	#return [2] + list(sieve) # unsorted

	res = [2] + list(sieve)
	res.sort()
	return res

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

###############################################################################
"""
Returns sorted list of primes up to n (inclusive).
Uses Sieve of Eratosthenes.

All primes > 3 have form 6k+1 or 6k+5.
Initialize sieve with these potential primes.
Sieve size is 2/6 = 33.3% of original, or 50% of size if we took only odds.
"""
def primes4(n: int) -> List[int]:
	if n < 2:
		return []
	if n == 2:
		return [2]
	if n == 3 or n == 4:
		return [2,3]

	end = int(n**0.5) + 1

	# "sieve" starts out as set of potential primes.
	# Doesn't include primes 2, 3.
	sieve = set(itertools.chain(
		range(5, n+1, 6), 
		range(7, n+1, 6),
		))

	for i in range(5, end, 2):
		if i in sieve:
			for j in range(i*i, n+1, 2*i):
				sieve.discard(j)
	
	#return [2,3] + [k for k in range(7, n+1, 2) if k in sieve] # sorted
	#return [2,3] + list(sieve) # unsorted
	
	res = [2,3] + list(sieve)
	res.sort()
	return res

###############################################################################
"""
Returns sorted list of primes up to n (inclusive).
Uses Sieve of Eratosthenes.

All primes > 5 have form 30k+d for d in (1,7,11,13,17,19,23,29).
Initialize sieve with these potential primes.

Sieve size is 8/30 = 26.7% size of original, or 80% of size if we took
possible primes of form 6+1 and 6k+5.
"""
def primes5(n: int) -> List[int]:
	if n < 2:
		return []
	if n == 2:
		return [2]
	if n == 3 or n == 4:
		return [2,3]
	if n == 5:
		return [2,3,5]

	end = int(n**0.5) + 1

	# "sieve" starts out as set of potential primes.
	# Doesn't include primes 2, 3, and 5.
	coprimes = (7,11,13,17,19,23,29,31)
	ranges = [range(k, n+1, 30) for k in coprimes]
	sieve = set(itertools.chain.from_iterable(ranges))

	for i in range(7, end, 2):
		if i in sieve:
			for j in range(i*i, n+1, 2*i):
				sieve.discard(j)
	
	# for i in range(0, end-30, 30):
	#     for d in (7, 11, 13, 17, 19, 23, 29, 31):
	#         j = i + d
	#         if j in sieve:
	#             for k in range(j*j, n+1, 2*j):
	#                 sieve.discard(k)

	#return [2,3,5] + [k for k in range(7, n+1, 2) if k in sieve] # sorted
	#return [2,3,5] + list(sieve) # unsorted
	
	res = [2,3,5] + list(sieve)
	res.sort()
	return res

"""
Returns sorted list of primes up to n (inclusive).
Uses Sieve of Eratosthenes.

All primes > 7 have form 210k+d for d in this list of 48 integers:
(1,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
101,103,107,109,113,121,127,131,137,139,143,149,151,157,163,167,169,
173,179,181,187,191,193,197,199,209).

Initialize sieve with these potential primes.

Sieve size is 48/210 = 22.86% of original, or 85.7% of size if we worked
with (2,3,5) instead of (2,3,5,7).
"""
def primes6(n: int) -> List[int]:
	if n < 2:
		return []
	if n == 3 or n ==4:
		return [2,3]
	if n == 5:
		return [2,3,5]
	if n == 7:
		return [2,3,5,7]

	end = int(n**0.5) + 1

	# "sieve" starts out as set of potential primes
	# doesn't include primes 2, 3, 5, 7
	# integers up to 210 coprime to 2, 3, 5, 7
	# For sake of creating ranges, we change 1 to 211.
	coprimes = (211,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,
		83,89,97,101,103,107,109,113,121,127,131,137,139,143,149,151,157,
		163,167,169,173,179,181,187,191,193,197,199,209)

	ranges = [range(k, n+1, 210) for k in coprimes]

	sieve = set(itertools.chain.from_iterable(ranges))

	for i in range(11, end, 2):
		if i in sieve:
			for j in range(i*i, n+1, 2*i):
				sieve.discard(j)
	
	# for i in range(0, end-30, 30):
	#     for delta in coprimes:
	#         j = i + delta
	#         if j in sieve:
	#             for k in range(j*j, n+1, 2*j):
	#                 sieve.discard(k)

	#return [2,3,5] + [k for k in range(7, n+1, 2) if k in sieve] # sorted
	#return [2,3,5] + list(sieve) # unsorted
	
	res = [2,3,5,7] + list(sieve)
	res.sort()
	return res

###############################################################################
"""
Korselt's criterion
Theorem (A. Korselt 1899): A positive composite integer n is a Carmichael 
number if and only if n is square-free, and for all prime divisors p of n, 
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

###############################################################################

if __name__ == "__main__":
	from timeit import default_timer as timer

	def print_primality(n=100):
		print(f"\nChecking for prime numbers up to {n}:")

		for i in range(1, n+1):
			if is_prime(i):
				print(i, end=", ")

		print()

	def test_primality(n=2**31-1):
		start = timer()
		res = is_prime5(n)
		t1 = timer() - start

		print("\nUsing method #5.")
		print(f"\nIs {n} prime? {res}")
		print(f"\nTook {t1}")

	def time_primality(n=2**31-1):
		start = timer()
		res1 = is_prime(n)
		t1 = timer() - start

		start = timer()
		res2 = is_prime2(n)
		t2 = timer() - start

		start = timer()
		res3 = is_prime3(n)
		t3 = timer() - start

		start = timer()
		res4 = is_prime4(n)
		t4 = timer() - start

		start = timer()
		res5 = is_prime5(n)
		t5 = timer() - start

		print(f"\nIs {n} prime?")
		print(f"Sol 1: {res1}")
		print(f"Sol 2: {res2}")
		print(f"Sol 3: {res3}")
		print(f"Sol 4: {res4}")
		print(f"Sol 5: {res5}")

		print(f"\nSol 1 took {t1}")
		print(f"Sol 2 took {t2}")
		print(f"Sol 3 took {t3}")
		print(f"Sol 4 took {t4}")
		print(f"Sol 5 took {t5}")

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
		sieve = primes4(n)
		print(f"\nSieve of Eratosthenes up to n = {n}:\n")
		print(f"First 10: {sieve[:10]}")
		print(f"Last 10: {sieve[-10:]}")
		print(f"Size: {len(sieve)}")

	def time_sieves(n=1000):
		start = timer()
		sieve = primes(n)
		t1 = timer() - start

		start = timer()
		sieve2 = primes2(n)
		t2 = timer() - start

		start = timer()
		sieve3 = primes3(n)
		t3 = timer() - start

		start = timer()
		sieve4 = primes4(n)
		t4 = timer() - start

		start = timer()
		sieve5 = primes5(n)
		t5 = timer() - start

		start = timer()
		sieve6 = primes6(n)
		t6 = timer() - start

		#sieve = sieve_of_eratosthenes(n)
		print(f"\nSieve of Eratosthenes up to n = {n}:")
		
		print(f"\n1 and 2 same? {sieve == sieve2}")
		print(f"\n1 and 3 same? {sieve == sieve3}")
		print(f"\n1 and 4 same? {sieve == sieve4}")
		print(f"\n1 and 5 same? {sieve == sieve5}")
		print(f"\n1 and 6 same? {sieve == sieve6}")

		print(f"\nFirst 10: {sieve[:10]}")
		print(f"Last 10: {sieve[-10:]}")
		
		# print(f"\nFirst 10: {sieve2[:10]}")
		# print(f"Last 10: {sieve2[-10:]}")

		print(f"\nSol 1 took {t1}")
		print(f"Sol 2 took {t2}")
		print(f"Sol 3 took {t3}")
		print(f"Sol 4 took {t4}")
		print(f"Sol 5 took {t5}")
		print(f"Sol 6 took {t6}")

	###

	#print_primality(1000)
	
	#test_primality()

	#time_primality(600851475143)
	#time_primality(6023223085147234351222922992431)
	#time_primality(2**53-1)
	#time_primality(2**59-1)

	#time_primality(6700417) # 7 digit prime, Euler
	#time_primality(2147483647) # 10 digit prime, Euler; Mersenne prime #8; 2^31 - 1
	#time_primality(67280421310721) # 14 digit prime
	#time_primality(2305843009213693951) # 19 digit prime; Mersenne #9; 2^61 -1
	
	#test_carmichael()
	
	#arr = {1, 2, 720, 1001, 2**31, 2*3*5*7*11*13*17*19*23*29*31, 600851475143}
	#for n in arr:
	#    test_prime_factors(n)    

	#test_prime_factorization(720)
	#test_prime_factorization(1001)
	#test_prime_factorization_arr(arr)
	#test_prime_factorization(10000000)

	#test_sieve(10000000)
	#test_sieve(1000)
	
	time_sieves(1000001)
	