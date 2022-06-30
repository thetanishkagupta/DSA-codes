class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        if root is None:
            return []
        ans = []
        queue = deque()
        # Add root node to Queue
        queue.append(root)
        while len(queue) != 0:
            node = queue.popleft()
            ans.append(node.data)
            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
        return ans
