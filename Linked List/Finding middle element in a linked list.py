'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
# Optimized Approach
class Solution:
    def findMid(self, head):
      # Take two pointers which points to head
      # iterate over linked list 
      # slow will move forward one time
      # fast will move forward two times
        fast = head
        slow = head
        if head is None:
            return 
        # For even condition: fast will point to Null and slow pointer will be middle.
        # For odd condition: when fast.next is NUll means fast will point to last node then slow pointer will be middle.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data    
