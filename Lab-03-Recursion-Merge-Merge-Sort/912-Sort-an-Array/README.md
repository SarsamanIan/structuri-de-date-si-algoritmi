 912. Sort an Array

- Platform: LeetCode
- Language: Python 3
- Status: Accepted
- Algorithm: Merge Sort

 Problem Description

Given an array of integers, sort the array in ascending order using the Merge Sort algorithm.

Built-in sorting functions are not used.

 Approach

The solution implements Merge Sort using recursion.

The algorithm follows three main steps:

1. Divide the array into two smaller parts.
2. Recursively sort both parts.
3. Merge the sorted parts using a temporary buffer.

The base case occurs when an interval contains one or zero elements.

A single shared buffer is allocated and reused during the merging process.

 Example

Input: [6, 2, 5, 2, 1]

Output: [1, 2, 2, 5, 6]

 Complexity

- Time Complexity: O(n log n)
- Space Complexity: O(n), including the temporary buffer and recursive call stack.

 LeetCode

https://leetcode.com/problems/sort-an-array/
