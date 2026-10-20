def is_in(lst: list, target: object) -> bool:
    """Linear search: check if target exists in lst by sequential scan.
    
    Time Complexity:
      - Best case:    O(1) (target is at index 0)
      - Worst case:   O(N) (target is at the end or not present)
      - Average case: O(N) (scans N/2 items on average)
    """
    for value in lst:
        if value == target:
            return True
    return False


def test_is_in():
    assert is_in([1, 2, 3], 3)
    assert not is_in([1, 2, 3], 4)
    assert is_in(["a", "b", "c"], "a")
    assert not is_in([], 1)


if __name__ == "__main__":
    test_is_in()
    print("All linear search (isin.py) tests passed successfully!")

