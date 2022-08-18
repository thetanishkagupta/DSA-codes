# Iterative Approach
class Solution(object):
    def reverseList(self, head):
        prev = None
        next = None
        curr = head
        while curr!= None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
