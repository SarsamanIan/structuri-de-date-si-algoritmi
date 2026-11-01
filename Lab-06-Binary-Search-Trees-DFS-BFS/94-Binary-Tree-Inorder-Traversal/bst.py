
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    result = []

    def dfs(node):
        if node is None:
            return

        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def tree_signature(node):
    if node is None:
        return None

    return (
        node.val,
        tree_signature(node.left),
        tree_signature(node.right)
    )


# Build the BST
def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    elif val > root.val:
        root.right = insert_into_bst(root.right, val)

    return root


def build_bst(values):
    root = None

    for val in values:
        root = insert_into_bst(root, val)

    return root


# Main test
values = [4, 2, 7, 1, 3, 6, 9]
root = build_bst(values)

print("BST test:")
print("Input:", values)
print("Expected: [1, 2, 3, 4, 6, 7, 9]")
print("Actual:  ", inorder(root))

# Check that the tree is not modified
before = tree_signature(root)
result = inorder(root)
after = tree_signature(root)

print("Tree unchanged:", before == after)


# Test: Non-BST tree
non_bst = TreeNode(2)
non_bst.left = TreeNode(1)
non_bst.right = TreeNode(3)
non_bst.left.left = TreeNode(4)

print("\nNon-BST tree:")
print("Expected: [4, 1, 2, 3]")
print("Actual:  ", inorder(non_bst))


# Test: Empty tree
print("\nEmpty tree:")
print("Expected: []")
print("Actual:  ", inorder(None))


# Test: Single node
single = TreeNode(10)

print("\nSingle node:")
print("Expected: [10]")
print("Actual:  ", inorder(single))


# Test: Left-only chain
left_chain = TreeNode(3)
left_chain.left = TreeNode(2)
left_chain.left.left = TreeNode(1)

print("\nLeft-only chain:")
print("Expected: [1, 2, 3]")
print("Actual:  ", inorder(left_chain))


# Test: Right-only chain
right_chain = TreeNode(1)
right_chain.right = TreeNode(2)
right_chain.right.right = TreeNode(3)

print("\nRight-only chain:")
print("Expected: [1, 2, 3]")
print("Actual:  ", inorder(right_chain))
