# GFG Solution
def delNode(head, k):
    if k==1:
       head=head.next
       return head
    else:
        pos = 1
        curr = head
        while curr:
            if pos==k-1:
                curr.next = curr.next.next
                break
            curr = curr.next
            pos += 1
        return head
      
      
#Leetcode solution
class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
      
