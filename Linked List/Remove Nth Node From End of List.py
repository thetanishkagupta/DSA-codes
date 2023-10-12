class Solution(object):
    def removeNthFromEnd(self, head, n):
        prev = head
        curr = head
        for i in range(n):
            # move curr pointer n number of times
            if curr.next:
                curr = curr.next
            else:
                return head.next
        while curr and curr.next:
            # when curr points to Null then return prev data
            curr = curr.next
            prev = prev.next
        prev.next = prev.next.next
        return head


# By using two pinter approach
class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        for i in range(n):  # move fast pointer till Nth term (fast pointer is N nodes ahead)
            fast = fast.next
        if fast == None:     # means node to be removed is head of list
            return slow.next
        while(fast.next != None):  
            slow = slow.next
            fast= fast.next
        slow.next = slow.next.next 
        return head


        
