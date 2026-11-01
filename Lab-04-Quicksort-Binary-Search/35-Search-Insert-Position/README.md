 35. Search Insert Position

**Platform:** LeetCode  
**Difficulty:** Easy  
**Topic:** Binary Search  
**Language:** Python 3  
**Status:** Accepted

 Approach

The solution uses Binary Search to find the position where the target should be inserted.

- If `nums[mid] < target`, search the right half.
- Otherwise, search the left half, including `mid`.
- When `lo == hi`, `lo` is the correct insertion position.

 Complexity Analysis

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
