class ListNode:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = next

def merge_k_lists(lists: list) -> ListNode:
    '''
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.
    '''
