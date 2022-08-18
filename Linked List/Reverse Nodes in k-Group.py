# GFG solution
# Reverse a Linked List in groups of given size.

class Solution:
    def reverse(self,head, k):
        prev = None
        curr = head
        next = None
        count = 0
        # reversing k size group
        while curr != None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        # Recursive call for the rest of the linked list
        if next is not None:
            head.next = self.reverse(next, k)
        return prev    
            
# Leetcode Solution        
# Reverse Nodes in k-Group  
class Solution(object):
    def length(self,head):
        l = 0
        curr = head
        
        while(curr):
            curr = curr.next
            l += 1
            
        return l
    def reverseKGroup(self, head, k):
        prev = None
        curr = head
        next = None
        count = 0
        
        if self.length(head) >= k:
            while curr != None and count < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count += 1
            if next is not None:
                head.next = self.reverseKGroup(next,k)
            return prev  
        else:
            return head
        
