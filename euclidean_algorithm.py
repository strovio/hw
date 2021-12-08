a, b = [int(s) for s in input().split()]

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
        
print("gcd(a,b) =", a + b)
