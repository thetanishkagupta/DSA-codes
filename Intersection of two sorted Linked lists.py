# Input:
# L1 = 1->2->3->4->6
# L2 = 2->4->6->8
# Output: 2 4 6

def findIntersection(head1,head2):
    if head1 == None or head2 == None:
        return None
    result = linkedList()
    
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            head1 = head1.next
            
        elif head1.data == head2.data:
            result.insert(head1.data)
            head1 = head1.next
            head2 = head2.next
            
        elif head2.data < head1.data:
            head2 = head2.next
            
    return result.head
