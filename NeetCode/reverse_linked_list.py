def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # Given the head of a linked list, return a reversed list.
    # Set the current node to the head of the list
    current = head
    prev = None
    # Make the node that current points to point to current
    while current:
        # save ref to cur.next
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev