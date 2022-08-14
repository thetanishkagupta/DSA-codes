class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        slow = head
        fast = head
        loop_found = False
        if head is None:
            return False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop_found = True
                break
        if loop_found is True:
            slow = head
            if slow == fast:
                while fast.next != slow:
                    fast = fast.next
            else:        
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next
            fast.next = None
        return 1
