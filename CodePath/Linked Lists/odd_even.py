'''
Given the head of a singly linked list, group all the
nodes with odd indices together followed by the nodes
with even indices, and return the reordered list.

The first node is odd and the second is even and so on.
The relative order inside the groups should remain the same.

Must be solved in O(1) space complexity + O(n) time complexity

If we didn't have this restriction, we could just use a multiple-pass
algorithm to add all the odd nodes onto a new list, and then go through
the list again to put on all the even nodes. But this would be O(n) space
'''

def odd_even(head):

    if not head or not head.next:
        return head

    odd_pointer = head # Keep a reference to the odd

    even_pointer = head.next # Keep two references to the even; one for the start and one to iterate
    even_head = head.next

    while odd_pointer.next and even_pointer.next:
        odd_pointer.next = odd_pointer.next.next
        odd_pointer = odd_pointer.next

        even_pointer.next = even_pointer.next.next
        even_pointer = even_pointer.next
    odd_pointer.next = even_head
    return head