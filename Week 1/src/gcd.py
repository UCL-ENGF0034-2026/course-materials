def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor using Euclid's subtraction algorithm."""
    if not (a > 0 and b > 0):
        raise ValueError(f"Inputs {a}, {b} must be positive integers.")
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# Provide GCD alias for mathematical / slide consistency
GCD = gcd