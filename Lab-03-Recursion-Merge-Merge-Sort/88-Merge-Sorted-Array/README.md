 88. Merge Sorted Array

- Platform: LeetCode
- Language: Python 3
- Status: Accepted

 Problem Description

Given two sorted integer arrays, merge nums2 into nums1 as one sorted array.

The first m elements of nums1 contain valid values. The remaining positions are available for the merged result.

 Approach

The solution uses three pointers:

- `i` points to the last valid element in nums1.
- `j` points to the last element in nums2.
- `k` points to the last available output position in nums1.

The algorithm compares elements from the end and writes the larger value into nums1.

Any remaining elements from nums2 are copied into nums1.

Merging from the back prevents overwriting unread values.

 Complexity

- Time Complexity: O(m + n)
- Space Complexity: O(1)

 Example

Input:
- nums1 = [2, 5, 6, 0, 0, 0]
- m = 3
- nums2 = [1, 2, 4]
- n = 3

Output: [1, 2, 2, 4, 5, 6]

## LeetCode

https://leetcode.com/problems/merge-sorted-array/
