'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

U: Find the closest node to the root that has no children 

M: DFS or BFS will work

P: Form a recursive solution

If there is a leaf, then

because we need to keep a minDepth

'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root) -> int:
        min_depth = float('inf')
        # Base case
        # There is no root so minDepth = 0
        if root is None:
            return 0
        
        # Node has 0 children
        elif root.left is None and root.right is None:
            return 1
        
        # Recursive
        # We don't need to add 1 in each recursive call
        # Case: We have 1 child, so we check both
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right))
        
        return min_depth + 1 # Account for root node in depth
