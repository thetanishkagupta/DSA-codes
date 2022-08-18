# GFG Solution
#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    temp1 = head1
    temp2 = head2
    intersect ={}
    while temp1 is not None:
        intersect[temp1] = 1
        temp1 = temp1.next
    while temp2 is not None:
        if temp2 in intersect:
            return temp2.data
        temp2 = temp2.next
    return -1  
  
  
  # leetcode solution
  class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        temp2 = headB
        dic = {}
        while temp1 is not None:
            dic[temp1] = 1
            temp1 = temp1.next
        while temp2 is not None:
            if temp2 in dic:
                return temp2
            temp2 = temp2.next
        return None    
