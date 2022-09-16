class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        queue = [root]
        depth = 1
        while len(queue)!= 0:
            l  = len(queue)
            for i in range(l):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return depth
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            depth += 1
        return depth
