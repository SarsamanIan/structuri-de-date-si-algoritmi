 1342. Number of Steps to Reduce a Number to Zero

- Platform: LeetCode
- Language: Python 3
- Status: Accepted

 Problem Description

Given an integer, count the number of steps required to reduce it to zero.

- If the number is even, divide it by 2.
- If the number is odd, subtract 1.
- Stop when the number becomes zero.

 Approach

The solution uses recursion.

The base case is `num == 0`, which returns 0.

For an even number, the function calls itself with `num // 2`.

For an odd number, the function calls itself with `num - 1`.

Each recursive call adds one step to the result.

 Complexity

- Time Complexity: O(log n)
- Space Complexity: O(log n), including the recursive call stack.

 Example

Input: 14

Output: 6

 LeetCode

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
