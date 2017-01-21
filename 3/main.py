import math
def isPrime(x):
    i=2
    while i <= x**(0.5):
        if x % i == 0:
            return False
        i+=1
    return True

BIG_NUMBER = 600851475143
for i in range(0, math.ceil(600851475143 ** 0.5))[::-1]:
    if BIG_NUMBER % i == 0 and isPrime(i):
        print(i)
        break
