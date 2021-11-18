    '''
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.
    '''
class ListNode:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = next


def merge_k_lists(lists: list) -> ListNode:
    '''
    Brute Force: traverse all the linked lists and collect the values of the nodes into an array
    Sort and interate over the resulting array to get value of nodes
    Create a new sorted linked list and extend it with the new nodes
    '''
def merge_k_lists(lists: list) -> ListNode:
    ''''''