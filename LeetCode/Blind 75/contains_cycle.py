'''
How to solve: Keep track of nodes we've seen before with a set.
'''

class LinkedListNode(object):
    # 3 -> 4 -> 6 -> 0 - > ...
    def __init__(self) -> None:
        self.value = value
        self.next = None
        # O(n)
        # start -> end
        # prev
        # curr
        # Cycle: when a node's next points to any previous node in the list
        def contains_cycle(linked_list):
            next_set = set()

            for node in linked_list:
                if next_set.add(node) == True:
                    return False

                return True
