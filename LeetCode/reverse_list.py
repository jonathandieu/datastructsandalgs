# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Change the current node's Next pointer to point to its previous
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # Previous is initially set to Null
        current = head # Save the head with a temp variable

        while current: # While the head exists
            next = current.next # Save the state of the next node (of the current) with a variable
            current.next = prev # Overwrite the next node with the previous node (that we declared earlier)
            prev = current # Update the previous node to be the current (so that we can reference it on the next loop)
            current = next # Move the iteration forward by setting current equal to its next that we saved earlier
        return prev # At the end of the loop, this becomes the head of our new list