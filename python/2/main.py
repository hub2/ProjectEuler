curr1 = 1
curr2 = 2
suma = 0
while curr2 < 4 * 10**6:
    if curr2 % 2 == 0:
        suma += curr2
    curr1, curr2 = curr2, curr1+curr2

print(suma)
