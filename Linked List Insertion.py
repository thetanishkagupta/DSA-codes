'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        temp = Node(x)
        temp.next = head
        head = temp
        return head
           
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        p = head
        if p is None:           # if no node exist in the linked list
            temp = Node(x)
            head = temp
        else:                   # if node is present in the linked list to insert at the end                      
            while p.next != None:
                p = p.next
            temp = Node(x)
            p.next = temp
        return head    
                
