class ListNode():
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
def merge_sorted_linked_lists(list1, list2):
    # Create a dummy node to avoid edge cases
    dummy = ListNode()
    curr = dummy

    # Iterate through both linked lists, comparing their values
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    # Handle the case where the lists are not the same size, so leftover list1 or list2 needs to be appended
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    # Return the list that was appended to the dummy node
    return dummy.next
