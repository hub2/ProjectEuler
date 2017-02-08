import math
from functools import *
def solution3(max_range):
    holder = [2]
    for i in range(2,max_range+1):
        if(len(list(filter(lambda x: i % x != 0,holder))) < len(holder)):
            continue
        else:
            holder.append(i)
    final = list(map(lambda x: pow(x,math.floor(math.log(max_range,x))),holder))
    prod = print(reduce(lambda x,y: x*y,final))
solution3(20000)
