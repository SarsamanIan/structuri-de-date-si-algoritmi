
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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


# Print the tree using inorder traversal
def inorder(root):
    if root is None:
        return []

    return inorder(root.left) + [root.val] + inorder(root.right)


# Main test
values = [4, 2, 7, 1, 3, 6, 9]

root = build_bst(values)

print("Input:", values)
print("Inorder traversal:", inorder(root))

# Test inserting 5 into a fresh tree
new_root = build_bst(values)
new_root = insert_into_bst(new_root, 5)

print("After inserting 5:", inorder(new_root))

# Additional tests
test_cases = [
    [],
    [5],
    [-5, -2, -8, 0],
    [4, 2, 4, 1, 2],
    [1, 2, 3, 4]
]

print("\nAdditional tests:")

for test in test_cases:
    test_root = build_bst(test)

    print("Input:", test)
    print("Output:", inorder(test_root))
    print("--------------------")
