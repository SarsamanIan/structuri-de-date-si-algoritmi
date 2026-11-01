
def partition(values, lo, hi):
    pivot = values[lo]
    boundary = lo

    for scan in range(lo + 1, hi):
        if values[scan] < pivot:
            boundary += 1
            values[boundary], values[scan] = values[scan], values[boundary]

    values[lo], values[boundary] = values[boundary], values[lo]

    return boundary


def quicksort(values, lo, hi):
    if hi - lo <= 1:
        return

    p = partition(values, lo, hi)

    quicksort(values, lo, p)
    quicksort(values, p + 1, hi)


def sort_array(values):
    quicksort(values, 0, len(values))
    return values


# Tests
test_cases = [
    [],
    [5],
    [-3, 7, -1, 0, 4],
    [4, 2, 4, 1, 2],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 2, 2, 2, 2]
]

for test in test_cases:
    original = test.copy()
    result = sort_array(test)

    print("Initial:", original)
    print("Sorted: ", result)
    print("Correct:", result == sorted(original))
    print("--------------------")
