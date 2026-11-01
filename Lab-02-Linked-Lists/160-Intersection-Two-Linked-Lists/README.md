 160. Intersection of Two Linked Lists

- Platform: LeetCode
- Language: Python 3
- Status: Accepted

 Problem Description

Given the heads of two singly linked lists, find the node at which the two lists intersect.

If the two linked lists do not intersect, return `None`.

 Approach

The solution uses two pointers:

- `pointerA` starts at the beginning of the first list.
- `pointerB` starts at the beginning of the second list.
- When a pointer reaches the end of its list, it switches to the beginning of the other list.
- If an intersection exists, both pointers meet at the same node.
- If there is no intersection, both pointers eventually become `None`.

 Complexity

- Time Complexity: O(n + m)
- Space Complexity: O(1)

 LeetCode

https://leetcode.com/problems/intersection-of-two-linked-lists/
