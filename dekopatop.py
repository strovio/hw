def repeat(n):
    def decorator(f):
        def wrapper(x):
            for i in range(n):
                x = f(x)
            return x
        return wrapper
    return decorator

@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
