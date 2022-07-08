class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        depth = 0
        q = []
        q.append(root)
        while q:
            depth += 1
            temp = [] # whatever we pop out , add its children to temp list
            
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp 
            
        return depth   
