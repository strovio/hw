def bezout(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = bezout(b, a % b)
    return (x, y - (a // b) * x, g)

a, b = [int(s) for s in input().split()]

print( "(x, y, gcd(a,b)) =",bezout(a, b))
