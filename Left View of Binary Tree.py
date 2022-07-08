def LeftView(root):
    result =[]
    if root is None:
        return result
        
    q = deque([])
    q.append(root)
    while q:
        level_size = len(q)
        for i in range(1,level_size + 1):
            node = q.popleft()
            
            if i==1:
                result.append(node.data)
                
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
                
    return result 
