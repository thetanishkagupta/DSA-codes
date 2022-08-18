# 1->2->3->4
# Adding dummy node '0' at the beginning
# 0->1->2->3->4

# d  p  q    p is head
# |  |  |
# 0->1->2->3->4
# d.next = head
# p = d.next
# q = p.next or d.next.next


# d  p  q    p is head
# |  |  |
# d->1->2->3->4

# d.next = q
# p.next = q.next
# q.next = p
# d=p

# d  q  p    
# |  |  |
# d->2->1->3->4 
#       |  |  |
#       d  p  q


class Solution(object):
    def swapPairs(self, head):
        dummy = d = ListNode(0)
        d.next = head
        
        while d.next and d.next.next is not None:
            p = d.next 
            q = p.next
            d.next, p.next, q.next = q, q.next, p
            d = p
        return dummy.next  
      
