94. Binary Tree Inorder Traversal

Platform: LeetCode  
Difficulty: Easy  
Topic: DFS - Inorder Traversal  
Language: Python 3  
Status: Accepted

 Approach

The solution uses recursive Depth First Search (DFS).

The traversal follows three steps:
1. Visit the left subtree.
2. Add the current node's value to the result.
3. Visit the right subtree.

A single shared result list is used to avoid creating new lists during recursive calls.

 Local Tests

The implementation was tested with:
- The BST built in Problem 1
- A binary tree that is not a BST
- An empty tree
- A single-node tree
- A left-only chain
- A right-only chain

The traversal does not modify the original tree or its child links.

 Example

Input tree:

```text
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

Output:

`[1, 2, 3, 4, 6, 7, 9]`

For the non-BST example:

```text
    2
   / \
  1   3
 /
4
```

Output:

`[4, 1, 2, 3]`

Inorder traversal does not sort arbitrary binary trees. It follows the existing child links.

Complexity Analysis

- Time Complexity: O(n)
- Recursive Auxiliary Space: O(h + 1)
- Output Storage: O(n)

Every node is visited exactly once.
LeetCode link: https://leetcode.com/problems/binary-tree-inorder-traversal/
