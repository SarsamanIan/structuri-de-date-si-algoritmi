 701. Insert into a Binary Search Tree

Platform: LeetCode  
Difficulty: Medium  
Topic: Binary Search Tree  
Language: Python 3  
Status: Accepted

 Description

The task is to insert a new value into a Binary Search Tree while preserving the BST property.

- Values smaller than the current node go to the left subtree.
- Values greater than the current node go to the right subtree.
- A new node is inserted when an empty position is found.
- Duplicate values leave the local tree unchanged.

 Local Implementation

The local implementation includes:
- `TreeNode` class
- `insert_into_bst()` function
- `build_bst()` function
- Inorder traversal for checking the tree
- Additional test cases

 Example

Input:

`[4, 2, 7, 1, 3, 6, 9]`

Expected BST:

```text
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

Inorder traversal:

`[1, 2, 3, 4, 6, 7, 9]`

After inserting 5 into a fresh tree:

`[1, 2, 3, 4, 5, 6, 7, 9]`

 Test Cases

- Empty input
- Single value
- Negative values
- Duplicate values
- Sorted input `[1, 2, 3, 4]`

All local tests passed.

 Complexity Analysis

Single insertion:
- Time: O(h + 1)
- Recursive auxiliary space: O(h + 1)

Building a tree with n values:
- Worst case: O(n²)
- Balanced construction: O(n log n)

Storage:
- Tree nodes: O(n)

An ordinary Binary Search Tree does not guarantee balance. Sorted input can produce a one-sided chain.
