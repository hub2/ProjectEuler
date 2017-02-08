from functools import *
print(reduce(lambda x,y:x*y, [(a,b,c) for c in range(1,998) for b in range(1,c) for a in range(1,b) if a**2 + b**2 == c**2 and a<b<c and a+b+c==1000][0]))

