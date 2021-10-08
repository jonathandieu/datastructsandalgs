def find_bad_revision(known_good: int, known_bad: int) -> int:
    # If we haven't narrowed the problematic code to one version, keep searching for the change-over point
    while known_bad - known_good > 1:
        mid = # get midpoint
        if is_bad(known_good + mid):
            known_bad = known_good + mid
        else:
            known_good = known_good + mid
    return known_bad

def is_binary_search_tree(root: Node) -> bool:
    def is_bst_helper(node: Node, min: float, max: float) -> bool:
        # Base case
        if node is None:
            return True
        