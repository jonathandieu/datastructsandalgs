'''
Write a function to delete a node in a singly-linked list
given access to the node to be deleted directly, not the HEAD.
It's guaranteed that the node to be deleted is NOT the tail node.
'''

# Because we aren't given the HEAD of the list, we must instead alter
# the actual values of the linked list and remove the node with next references.
def delete_node(node):
	node.value = node.next.value
	node.next = node.next.next
