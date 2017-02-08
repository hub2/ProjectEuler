count = 0
with open("triangles.txt") as f:
    for line in f:
        data = line.split(",")
        data = [int(x) for x in data]
        x1,y1 = data[0], data[1]
        x2,y2 = data[2], data[3]
        x3,y3 = data[4], data[5]
        a = float((y2-y3)*(-x3) + (x3-x2)*(-y3)) / ((y2-y3)*(x1-x3) + (x3-x2)*(y1-y3))
        b = float((y3-y1)*(-x3) + (x1-x3)*(-y3)) / ((y2-y3)*(x1-x3) + (x3-x2)*(y1-y3))
        c = 1 - a - b
        if 0<=a<=1 and 0<=b<=1 and 0<=c<=1:
            count += 1
print(count)
