# Linked Lists

**Time Complexity:**
Best case: `O(1)` for Accessing/Search
O(1) Deleting/Inserting at head
Worst case: `O(n)` Linear

**Node:** A position in the list that contains the value of whatever's stored at the position as well as at least one reference to another node
**Head:** node at the beginning of the list
**Tail:** Node at the end of the list
**Sentinel:** dummy node, typically placed at the head or end of the list to help make operations simpler (like delete) or to indicate the end of the list.

Example class definition:

```py
 class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
```
## Common Operations
```py
def insert(self, val):
    node = ListNode(val)
    node.next = self
    return n
```
```py
```
```py
```

# Linked List Techniques
## Multiple Passes

## Dummy Head
Used more like a hack, and are commonly used to avoid writing additional code for edge cases.

Use this to save yourself the creation of special edge conditions with some algorithms. It involves creating one extra pointer, the dummy head, that will point to your final answer or list that you will return.
