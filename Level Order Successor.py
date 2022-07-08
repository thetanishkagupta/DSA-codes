class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        
def level_order_Successor(root,key):
    if root is None:
        return None
    queue = []
    queue.append(root)
    while len(queue) != 0:
        current = queue.pop(0)
            
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
                
        if current == key:
            break
            
    return queue[0]
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
key = root.left.left
res = level_order_Successor(root,key)
if res:
    print("LevelOrder successor of " + str(key.data) + " is " + str(res.data))
     
else:
    print("LevelOrder successor of " + str(key.data) + " is NULL")
        
