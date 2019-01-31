
import math
from functools import reduce


# Euclidean algorithm
def gcd(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp

    return x


def gcd_recursive(x, y):
    if y == 0:
        return x
    else:
        return gcd_recursive(y, x % y)


def lcm(x, y):
    return int(x * y / gcd(x, y))



tests = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), 
    (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
    (1071, 462)
    ] 


for x, y in tests:
    print("gcd({}, {}) = {}".format(x, y, gcd(x,y)))
    print("gcd_recursive({}, {}) = {}".format(x, y, gcd_recursive(x,y)))

for x, y in tests:
    print("lcm({}, {}) = {}".format(x, y, lcm(x,y)))


