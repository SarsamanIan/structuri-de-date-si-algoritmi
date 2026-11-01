206. Reverse Linked List

- Platform: LeetCode
- Language: Python 3
- Status: Accepted

Problem Description

Given the head of a singly linked list, reverse the list and return the new head.

Approach

The solution uses three pointers:

- `previous` stores the previous node.
- `current` represents the current node.
- `next_node` temporarily stores the next node.

At each iteration, the direction of the link is reversed. The process continues until all nodes have been visited.

 Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

 LeetCode

https://leetcode.com/problems/reverse-linked-list/
