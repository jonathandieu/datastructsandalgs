# Class Definitions
class Node():
    data = None
    right = None
    left = None
    def __init__(self, data: int):
        self.data = data



# def find_bad_revision(known_good: int, known_bad: int) -> int:
#     # If we haven't narrowed the problematic code to one version, keep searching for the change-over point
#     while known_bad - known_good > 1:
#         mid = (known_good + known_bad) / 2# get midpoint
#         if is_bad(known_good + mid):
#             known_bad = known_good + mid
#         else:
#             known_good = known_good + mid
#     return known_bad


# Function to determine whether or not a BST is valid
# A BST is valid if every value smaller than the root exists to the left and every value to the right is larger
# Edge case: empty tree (single node) is still valid
def is_binary_search_tree(root: Node) -> bool:
    def is_bst_helper(node: Node, min: float, max: float) -> bool:
        # Base case
        if node is None:
            return True
