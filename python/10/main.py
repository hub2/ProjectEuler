def isPrime(x):
    i=2
    while i <= x**(0.5):
        if x % i == 0:
            return False
        i+=1
    return True
suma = 0
for i in range(2, 2* (10**6)):
    if (isPrime(i)):
        suma += i
print(suma)
