#  rotate the list to the right by k places.

class Solution(object):
    def rotateRight(self, head, k):
        if head==None or head.next==None or k==0:
            return head
        # finding length of list
        length=1
        curr=head
        while curr.next!=None:
            length+=1
            curr=curr.next
        # finding point of start of rotation
        curr.next=head
        rotations=int(k%length)
        rotations=length-rotations
        while rotations!=0:
            curr=curr.next
            rotations-=1
        head=curr.next  
        curr.next=None
        return head
