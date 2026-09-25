import sys


def gcd(a: int, b: int) -> int:
    """Compute the GCD of two positive integers."""
    if not (a > 0 and b > 0):
        raise ValueError(f"Inputs {a}, {b} must be positive integers.")
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


GCD = gcd


# Test cases for function
def test_euclid() -> None:
    ax = 42
    bx = 30
    assert gcd(ax, bx) == 6
    assert gcd(bx, ax) == 6


def test_euclid_exc() -> None:
    try:
        gcd(5, -1)
        assert False, "Expected ValueError was not raised."
    except ValueError as e:
        assert "must be positive" in str(e).lower()
    finally:
        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Euclid requires two arguments.")
    else:
        try:
            ax = int(sys.argv[1])
            bx = int(sys.argv[2])
        except ValueError:
            print("Euclid requires two integers.")
        else:
            try:
                print(gcd(ax, bx))
            except ValueError:
                print("Euclid requires positive integers.")
