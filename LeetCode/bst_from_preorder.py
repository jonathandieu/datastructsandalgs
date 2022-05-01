"""
First item in preorder list is the root to be considered.
For next item in preorder list, there are 2 cases to consider:
If value is less than last item in stack, it is the left child of last item.
If value is greater than last item in stack, pop it.
The last popped item will be the parent and the item will be the right child of the parent.
"""

def bst_from_preorder(preorder: list):
    pass