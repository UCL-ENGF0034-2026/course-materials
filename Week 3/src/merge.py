def mergesort(lst, compare=lambda a, b: a <= b):
    """Divide and conquer Merge Sort.
    
    Splits the list at the midpoint, sorts each half recursively,
    and merges the two sorted sublists.
    Time Complexity:  O(N log N) in all cases.
    Space Complexity: O(N) auxiliary memory.
    """
    if len(lst) <= 1:
        return lst
    pivot = len(lst) // 2
    lst1 = mergesort(lst[:pivot], compare)
    lst2 = mergesort(lst[pivot:], compare)
    return merge(lst1, lst2, compare)


def merge(lst1, lst2, compare=lambda a, b: a <= b):
    """Linear-time two-pointer merge combining two sorted lists into one."""
    merged_list = []
    index1 = 0
    index2 = 0
    len1 = len(lst1)
    len2 = len(lst2)

    while index1 < len1 or index2 < len2:
        if index2 == len2 or (
            index1 < len1 and compare(lst1[index1], lst2[index2])
        ):
            merged_list.append(lst1[index1])
            index1 += 1
        else:
            merged_list.append(lst2[index2])
            index2 += 1

    return merged_list


def cmp_str(s1, s2):
    """Case-insensitive string comparator. Uses <= to preserve stability on ties."""
    return s1.lower() <= s2.lower()


def test_sortstr():
    assert mergesort(["abc"], cmp_str) == ["abc"]
    assert mergesort(["BA", "aa", "bbbb", "a"], cmp_str) == [
        "a", "aa", "BA", "bbbb"
    ]
    assert mergesort(
        ["BAAAAA", "aa", "bbbb", "a"],
        lambda x, y: len(x) <= len(y)
    ) == ["a", "aa", "bbbb", "BAAAAA"]

    # Verify stability: equal scores preserve relative arrival order
    records = [("Alice", 10), ("Bob", 5), ("Charlie", 10)]
    assert mergesort(records, lambda a, b: a[1] <= b[1]) == [
        ("Bob", 5), ("Alice", 10), ("Charlie", 10)
    ]


if __name__ == "__main__":
    test_sortstr()
    print("All Merge Sort (merge.py) tests passed successfully!")
    
