
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# BST insertion
def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    elif val > root.val:
        root.right = insert_into_bst(root.right, val)

    return root


# Build BST
def build_bst(values):
    root = None

    for val in values:
        root = insert_into_bst(root, val)

    return root


# BFS - Level Order Traversal
def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# Tree structure signature
def tree_signature(node):
    if node is None:
        return None

    return (
        node.val,
        tree_signature(node.left),
        tree_signature(node.right)
    )


# BFS trace
def trace_bfs(root):
    if root is None:
        print("Empty tree - queue is empty.")
        return

    queue = deque([root])
    level_number = 1

    print("\nBFS QUEUE TRACE")

    while queue:
        level_size = len(queue)
        level = []

        print("\nLevel", level_number)
        print("Queue at level start:",
              [node.val for node in queue])
        print("Nodes to remove:", level_size)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            print(
                "Removed:", node.val,
                "| Level:", level,
                "| Queue after adding children:",
                [item.val for item in queue]
            )

        print("Completed level:", level)
        level_number += 1


# Main BST test - Problem 701
values = [4, 2, 7, 1, 3, 6, 9]
root = build_bst(values)

print("MAIN BST TEST")
print("Input:", values)
print("Expected: [[4], [2, 7], [1, 3, 6, 9]]")
print("Actual:  ", level_order(root))


# Check that the tree is unchanged
before = tree_signature(root)
result = level_order(root)
after = tree_signature(root)

print("Tree unchanged:", before == after)


# BFS queue trace
trace_bfs(root)


# Test: Empty tree
print("\nEMPTY TREE TEST")
print("Expected: []")
print("Actual:  ", level_order(None))


# Test: Single node
single = TreeNode(10)

print("\nSINGLE NODE TEST")
print("Expected: [[10]]")
print("Actual:  ", level_order(single))


# Test: Chain
chain = TreeNode(1)
chain.right = TreeNode(2)
chain.right.right = TreeNode(3)

print("\nCHAIN TEST")
print("Expected: [[1], [2], [3]]")
print("Actual:  ", level_order(chain))


# Test: Non-BST tree from Problem 94
non_bst = TreeNode(2)
non_bst.left = TreeNode(1)
non_bst.right = TreeNode(3)
non_bst.left.left = TreeNode(4)

print("\nNON-BST TREE TEST")
print("Expected: [[2], [1, 3], [4]]")
print("Actual:  ", level_order(non_bst))

before = tree_signature(non_bst)
level_order(non_bst)
after = tree_signature(non_bst)

print("Tree unchanged:", before == after)
