divisors = 0
i = 1
tr_number = 0
while divisors <= 500:
    tr_number += i
    #divisors = len(filter(lambda x: not tr_number % x, range(1,tr_number+1)))
    #print(tr_number, divisors)
    i+=1
print(tr_number)
