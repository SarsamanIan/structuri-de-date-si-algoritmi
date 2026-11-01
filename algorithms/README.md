 Quicksort Algorithm

 Implementation

Quicksort is a sorting algorithm based on the divide-and-conquer approach.

The implementation uses the first element of the current interval as the pivot.

The partition function uses a half-open interval `[lo, hi)`:
- `pivot = values[lo]` selects the first element as the pivot.
- `boundary` tracks the position of elements smaller than the pivot.
- `scan` checks the remaining elements.
- Elements smaller than the pivot are moved to the left.
- Finally, the pivot is placed in its correct position.

Quicksort recursively sorts the intervals `[lo, p)` and `[p + 1, hi)`.

 Example

Initial array:

`[6, 2, 5, 2, 1]`

After the first partition:

`[1, 2, 5, 2, 6]`

Pivot position:

`p = 4`

Final sorted array:

`[1, 2, 2, 5, 6]`

 Test Cases

The implementation was tested with:
- Empty array
- Single-element array
- Negative numbers
- Duplicate values
- Already sorted array
- Reverse sorted array
- Array containing only equal values

All tests passed.

 Comparison with Merge Sort

Both algorithms were executed on separate copies of the same input:

`[6, 2, 5, 2, 1]`

Both produced:

`[1, 2, 2, 5, 6]`

The results were identical.

 Complexity Analysis

| Case | Time Complexity | Auxiliary Space |
|---|---|---|
| Average / Balanced | O(n log n) | O(log n) |
| Worst Case | O(n²) | O(n) |

The worst case occurs when the pivot repeatedly produces highly unbalanced partitions.

 Pivot Comparison Analysis

For `[1, 2, 3, 4, 5]`:

`4 + 3 + 2 + 1 = 10 comparisons`

For `[2, 2, 2, 2, 2]`:

`4 + 3 + 2 + 1 = 10 comparisons`

The strict comparison `< pivot` means equal elements remain on the right side of the pivot, which can lead to unbalanced partitions.
