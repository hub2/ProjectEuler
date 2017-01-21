from functools import *
def gcd(a, b):
    while b != 0:
        a,b = b, a%b
    return a

gcdResult = reduce(lambda x,y: x//gcd(x,y) * y, range(1,20))
print(gcdResult)
