def max_depth(root) -> int:
    if not root:
        return 0
    else:
        return max(maxDepth(root.left), maxDepth(root.right))