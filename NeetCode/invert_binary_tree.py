'''
Given the root of a binary tree, invert the tree, and return its root.
'''

def invert_binary_tree(root):

    # Base case:
    if not root:
        return None
    # Invert the left subtree
    # Invert the right subtree


    # OR
    if root:
        root.left, root.right = self.invert_binary_tree(root.right), self.invert_binary_tree(root.left)
        return root