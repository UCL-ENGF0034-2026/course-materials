import os


def is_in_bisect(lst: list, val: object) -> bool:
    """Returns True if val is within the sorted list lst using bisection.
    
    Maintains the half-open interval [start, end) where lst[start] <= val < lst[end].
    Time Complexity: O(log N) comparisons.
    """
    if len(lst) == 0:
        return False
    start = 0          # start of search range
    end = len(lst)     # end of search range
    while end - start > 1:
        middle = (start + end) // 2
        if val >= lst[middle]:
            start = middle
        else:
            end = middle
    return lst[start] == val


def test_is_in():
    assert not is_in_bisect([], 4)
    assert is_in_bisect([1], 1)
    assert is_in_bisect([1, 2, 3], 3)
    assert is_in_bisect([1, 2, 3], 2)
    assert is_in_bisect([1, 2, 3], 1)
    assert is_in_bisect([1, 2, 3, 4], 4)
    assert is_in_bisect([1, 2, 3, 4], 3)
    assert is_in_bisect([1, 2, 3, 4], 2)
    assert is_in_bisect([1, 2, 3, 4], 1)
    assert is_in_bisect([1, 2, 2, 2, 3], 2)
    assert is_in_bisect([2, 3, 4, 5, 6, 7], 3)
    assert not is_in_bisect([1, 2, 3, 3, 3, 10], 4)


def is_in_bisect_tikz(seq: list, val: object, pic_name: str) -> bool:
    """Returns True if val is within the sorted sequence seq, writing a TikZ trace."""
    dirname = os.path.dirname(pic_name)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    node_names = [f"n{i}" for i in range(len(seq) + 1)]

    with open(pic_name, "w") as f:
        f.write("\\begin{tikzpicture}\n")
        for i, name in enumerate(node_names):
            if i == 0:
                f.write(f"\\node ({name}) {{{seq[i]}}};\n")
                f.write(f"\\draw ({name}.north west) rectangle ({name}.south east);\n")
            elif i < len(seq):
                f.write(f"\\node [right=0.1cm of {node_names[i-1]}] ({name}) {{{seq[i]}}};\n")
                f.write(f"\\draw ({name}.north west) rectangle ({name}.south east);\n")
            else:
                f.write(f"\\node [right=0.1cm of {node_names[i-1]}] ({name}) {{}};\n")
                f.write(f"\\draw ({name}.north west) rectangle ({name}.south east);\n")

        range_start = 0
        range_end = len(seq)
        diff = range_end - range_start
        num = 1

        f.write(f"\\node<{num}> [above=0.2cm of {node_names[range_start]}] (s{num}) {{s}};\n")
        f.write(f"\\node<{num}> [above=0.2cm of {node_names[range_end]}] (e{num}) {{e}};\n")
        f.write(f"\\draw<{num}> [->] (s{num}) -- ({node_names[range_start]});\n")
        f.write(f"\\draw<{num}> [->] (e{num}) -- ({node_names[range_end]});\n")
        num += 1

        while diff > 1:
            f.write(f"\\node<{num}> [above=0.2cm of {node_names[range_start]}] (s{num}) {{s}};\n")
            f.write(f"\\node<{num}> [above=0.2cm of {node_names[range_end]}] (e{num}) {{e}};\n")
            f.write(f"\\draw<{num}> [->] (s{num}) -- ({node_names[range_start]});\n")
            f.write(f"\\draw<{num}> [->] (e{num}) -- ({node_names[range_end]});\n")

            range_mid = (range_start + range_end) // 2
            if seq[range_mid] <= val:
                range_start = range_mid
            else:
                range_end = range_mid

            f.write(f"\\node<{num}> [above=0.2cm of {node_names[range_mid]}] (m{num}) {{m}};\n")
            f.write(f"\\draw<{num}> [->] (m{num}) -- ({node_names[range_mid]});\n")
            num += 1

            assert diff > (range_end - range_start)  # Ensure progress
            diff = range_end - range_start

        f.write(f"\\node<{num}> [above=0.2cm of {node_names[range_start]}] (s{num}) {{s}};\n")
        f.write(f"\\node<{num}> [above=0.2cm of {node_names[range_end]}] (e{num}) {{e}};\n")
        f.write(f"\\draw<{num}> [->] (s{num}) -- ({node_names[range_start]});\n")
        f.write(f"\\draw<{num}> [->] (e{num}) -- ({node_names[range_end]});\n")
        f.write("\\end{tikzpicture}\n")

    return len(seq) > 0 and seq[range_start] == val


def test_is_in_tikz():
    array = [1, 1, 2, 5, 5, 10, 10, 11, 17, 17, 100, 110, 112, 117]
    assert is_in_bisect_tikz(array, 17, r"assets/binarysearch.tex")


if __name__ == "__main__":
    test_is_in()
    test_is_in_tikz()
    print("All binary search (binarysearch.py) tests passed successfully!")

