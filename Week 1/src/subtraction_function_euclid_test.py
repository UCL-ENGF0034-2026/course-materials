def gcd(a: int, b: int) -> int:
    """Compute the GCD of two positive integers."""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


GCD = gcd


def test_euclid() -> None:
    ax = 42
    bx = 30
    r = gcd(ax, bx)
    assert r == 6


if __name__ == "__main__":
    test_euclid()
    print("Tests passed.")