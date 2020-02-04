
import math
from functools import reduce
from itertools import accumulate


# Euclidean algorithm
def gcd(x, y):
    while y != 0:
        x, y = y, x % y

    return x

def gcd_recursive(x, y):
    if y == 0:
        return x
    else:
        return gcd_recursive(y, x % y)

def lcm(x, y):
    return int(x * y / gcd(x, y))

"""
Given array of positive integers, return all positive integers from 1 to
product(arr) that are coprime (relatively prime) to each element in array.
"""
def coprimes(arr):
    res = [1]
    end = 1 + reduce(lambda x,y: x*y, arr, 1)

    for i in range(2, end):
        for x in arr:
            if gcd(i, x) != 1:
                break
        else:
            res += [i]

    return res


###############################################################################

if __name__ == "__main__":
    tests = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), 
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
        (1071, 462)
        ] 

    # for x, y in tests:
    #     print("gcd({}, {}) = {}".format(x, y, gcd(x,y)))
    #     print("gcd_recursive({}, {}) = {}".format(x, y, gcd_recursive(x,y)))

    # for x, y in tests:
    #     print("lcm({}, {}) = {}".format(x, y, lcm(x,y)))

    #res = coprimes([2,3,5])
    res = coprimes([2,3,5,7])
    print(res)
    print(len(res))
