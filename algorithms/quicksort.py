
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
    
    
# Merge Sort implementation
def merge_sort(values):
    if len(values) <= 1:
        return values

    mid = len(values) // 2

    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Compare Quicksort and Merge Sort
numbers = [6, 2, 5, 2, 1]

quick_numbers = numbers.copy()
merge_numbers = numbers.copy()

sort_array(quick_numbers)
merge_numbers = merge_sort(merge_numbers)

print("\nAlgorithm comparison:")
print("Original:  ", numbers)
print("Quicksort: ", quick_numbers)
print("Merge Sort:", merge_numbers)
print("Same result:", quick_numbers == merge_numbers)
