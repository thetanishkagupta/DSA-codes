# Two pointer approach
class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        loop_found = False
        if head is None:
            return None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop_found = True
                break
        if loop_found is True:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow 
        return None

      
# Three pointer appraoch
class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        entry = head
        if head is None:
            return None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = entry
                entry = head
                while entry != fast:
                    entry = entry.next
                    fast = fast.next
                return entry 
        return None
