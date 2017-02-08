from z3 import *
x = Int('x')
y = Int('y')

def get_models(F):
    result = []
    s = Solver()
    s.add(F)
    while s.check() == sat:
        m = s.model()
        result.append(m)
        # Create a new constraint the blocks the current model
        block = []
        for d in m:
            # create a constant from declaration
            c = d()
            print(s,c, m[d])
            block.append(c != m[d])
        s.add(Or(block))
    return result

for i in range(4,10000):
    models = get_models([x+y == x*y*Q(1,i), x>=y, x>0, y>0])
    print(models)


