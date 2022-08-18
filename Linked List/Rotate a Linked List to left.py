class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        temp = head
        end_Node = None
        while temp.next != None:
            temp = temp.next
        temp.next = head
        i = 0
        while (i < k):
            temp = temp.next
            i+= 1
        head = temp.next
        temp.next = None
        return head
        
