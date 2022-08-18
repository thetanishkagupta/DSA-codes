#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    curr = head
    prev = head
    if head is None:
        return 
    for i in range(n):
        if curr is not None:
            curr = curr.next
        else:
            return -1
    while curr is not None:
        curr = curr.next
        prev = prev.next
    return prev.data  
