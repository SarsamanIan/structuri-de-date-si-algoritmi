 LeetCode 102 – Binary Tree Level Order Traversal

LeetCode: https://leetcode.com/problems/binary-tree-level-order-traversal/

Difficulty: Medium

 Problem Description

Given the root of a binary tree, return the level order traversal of its nodes' values.

The traversal visits nodes level by level, from left to right.

 Approach – Breadth-First Search (BFS)

The solution uses a FIFO queue implemented with Python's `collections.deque`.

Steps:
1. Add the root node to the queue.
2. Save the number of nodes currently in the queue.
3. Remove exactly that many nodes.
4. Add each node's value to the current level.
5. Add the left child, followed by the right child, if present.
6. Add the completed level to the result.
7. Repeat until the queue is empty.

 Tree Diagram

```text
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

Expected Output

```python
[[4], [2, 7], [1, 3, 6, 9]]
```

BFS Queue Trace

| Level | Queue at start | Nodes to remove | Level result |
|---|---|---:|---|
| 1 | [4] | 1 | [4] |
| 2 | [2, 7] | 2 | [2, 7] |
| 3 | [1, 3, 6, 9] | 4 | [1, 3, 6, 9] |

The local implementation also prints the queue after each node is removed and its children are added.

 Local Tests

- Empty tree: `[]`
- Single node: `[[10]]`
- Chain: `[[1], [2], [3]]`
- Non-BST tree from Problem 94: `[[2], [1, 3], [4]]`
- Main BST: `[[4], [2, 7], [1, 3, 6, 9]]`
- Tree unchanged after traversal: `True`

 Complexity Analysis

- Time Complexity: O(n) – each node enters and leaves the queue exactly once.
- Auxiliary Working Space: O(w) – the queue stores waiting nodes, where w is the maximum number of nodes on a level.
- Output Space: O(n) – the result stores all node values.

The queue uses `deque`, which supports O(1) insertion at the end and removal from the beginning.

 Files

- `solution.py` – LeetCode submission.
- `bst.py` – Local BST construction, BFS implementation, queue trace, and tests.
