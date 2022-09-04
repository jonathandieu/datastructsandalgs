def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Create queue
        from collections import deque
        q = deque()
        q.append(root)
        level_list = []

        # Edge Case:
        if not root:
            return []

        while q: # EACH LEVEL
            # process each level
            level = []
            for i in range(len(q)): # Item in the level
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            level_list.append(level)
        return level_list
