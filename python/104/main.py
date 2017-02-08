def isPandigital(x):
    for i in range(1,10):
        if str(i) not in x:
            return False
    return True


curr1 = 1
curr2 = 1
idx = 2

while True:
    idx+=1
    curr1, curr2 = curr2, curr1+curr2
    curr2str = str(curr2)
    #print(curr2str[:9], curr2str[-9:])
    if isPandigital(curr2str[:9]) and isPandigital(curr2str[-9:]):
        print(curr2)
        print(idx)
        break


