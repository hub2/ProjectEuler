def isPrime(x):
    i=2
    while i <= x**(0.5):
        if x % i == 0:
            return False
        i+=1
    return True
i=0
c=2
while True:
    if isPrime(c):
        i+=1
        print(i, c)
        if i == 10001:
            print(c)
            break
    c+=1
