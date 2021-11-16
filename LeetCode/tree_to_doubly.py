class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def tree_to_doubly(root: Node) -> Node:
    # Null check
    if root == None:
        head = Node()


node = Node(3)
print(node)
tree_to_doubly(node)