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
