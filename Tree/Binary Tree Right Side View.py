class Solution(object):
    def rightSideView(self, root):
        result = []
        if root is None:
            return None
        
        q = deque([])
        q.append(root)
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return result  
