ratio = 0
bouncy = 0
not_bouncy = 0
i = 1
def isNotBouncy(i):
    i = str(i)
    return "".join(sorted(i)) == i or "".join(sorted(i, reverse=True)) == i[::-1]
while ratio != 0.9:
    if isNotBouncy(i):
        not_bouncy += 1
    else:
        bouncy += 1
    i+=1
    ratio = not_bouncy/(bouncy + not_bouncy)
    print(bouncy, not_bouncy, ratio)
print(i)
