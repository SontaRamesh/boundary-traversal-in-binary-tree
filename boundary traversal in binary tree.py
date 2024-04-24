class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_left_boundary(root):
    if root:
        if root.left:
            print(root.val, end=" ")
            print_left_boundary(root.left)
        elif root.right:
            print(root.val, end=" ")
            print_left_boundary(root.right)

def print_leaves(root):
    if root:
        print_leaves(root.left)
        if root.left is None and root.right is None:
            print(root.val, end=" ")
        print_leaves(root.right)

def print_right_boundary(root):
    if root:
        if root.right:
            print_right_boundary(root.right)
            print(root.val, end=" ")

        elif root.left:
            print_right_boundary(root.left)
            print(root.val, end=" ")

def boundary_traversal(root):
    if root:
        print(root.val, end=" ")

        # Print the left boundary except the leaf node
        print_left_boundary(root.left)

        # Print all leaf nodes
        print_leaves(root)

        # Print the right boundary except the leaf node
        print_right_boundary(root.right)

# Example usage:
# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right=TreeNode(8)

# Print the boundary traversal
boundary_traversal(root)
