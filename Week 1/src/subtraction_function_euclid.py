def gcd(a: int, b: int) -> int:
    """Compute the GCD of two positive integers."""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


GCD = gcd

ax = 42
bx = 30
result = gcd(ax, bx)
print(result)