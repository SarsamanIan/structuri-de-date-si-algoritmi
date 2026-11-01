# 704. Binary Search

- Platform: LeetCode
- Language: Python 3
- Status: Accepted

 Problem Description

Given a sorted array of integers and a target value, return the index of the target if it exists. Otherwise, return -1.

 Approach

The solution uses iterative binary search with the interval [lo, hi).

- `lo` represents the beginning of the search interval.
- `hi` represents the exclusive end of the interval.
- `mid` represents the middle index.

At each iteration, half of the remaining search interval is eliminated.

If the middle value is smaller than the target, the search continues on the right.

If it is greater, the search continues on the left.

If the interval becomes empty, the function returns -1.

 Complexity

- Time Complexity: O(log n)
- Space Complexity: O(1)

 LeetCode

https://leetcode.com/problems/binary-search/
