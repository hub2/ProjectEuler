biggest = 0
for i in range(100, 999)[::-1]:
    for j in range(100, 999)[::-1]:
        tmp = str(i*j)
        if(tmp[::-1] == tmp and int(tmp) > biggest):
            biggest = int(tmp)

print(biggest)

