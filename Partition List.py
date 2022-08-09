class Solution(object):
    def partition(self, head, x):
        small_list = ListNode(0)  #  creating two empty list : small & high
        small = small_list        #  small will store the head.data < X
        high_list = ListNode(0)
        high = high_list          #  high will store the head.data > X
        
        while head != None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                high.next = head
                high = high.next
            head = head.next
        high.next = None    
        small.next = high_list.next  # merging both list
        return small_list.next       # removing 0 of small list
        
        
