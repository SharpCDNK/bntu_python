import math

def solveQuadratic(eqn, roots):
    a,b,c = eqn

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return -1
    elif discriminant == 0:
        roots.append(-b / (2 * a))
        return 1
    else:
        roots.append((-b - math.sqrt(discriminant)) / (2 * a))
        roots.append((-b + math.sqrt(discriminant)) / (2 * a))
        return 2

eqn = list(map(float,input("Enter a, b, c: ").split()))
roots = []

n = solveQuadratic(eqn,roots)

print("Counts of roots: ", n)

if n > 0:
    print("Roots: ",roots)



