from gcd import gcd


def test_gcd() -> None:
    ax = 42
    bx = 30
    v = gcd(ax, bx)
    assert v == 6


def test_gcd2() -> None:
    ax = 6
    bx = 6
    v = gcd(ax, bx)
    assert v == 6


def test_gcd3() -> None:
    ax = 42
    bx = -30
    try:
        gcd(ax, bx)
        assert False, "Expected ValueError was not raised."
    except ValueError as e:
        assert "must be positive" in str(e).lower()
    finally:
        pass


if __name__ == "__main__":
    test_gcd()
    test_gcd2()
    test_gcd3()
    print("All tests passed.")