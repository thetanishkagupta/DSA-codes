class Solution(object):
    def findmaxsum(self,root):
        if root is None:
            return 0
        leftsum = self.findmaxsum(root.left)
        rightsum = self.findmaxsum(root.right)
        
        leftsum = max(leftsum, 0)
        rightsum = max(rightsum, 0)
        
        currentsum = leftsum + rightsum + root.val
        self.maxsum = max(currentsum , self.maxsum)
        
        return max(leftsum, rightsum) + root.val
    
        
    def maxPathSum(self, root):
        self.maxsum = -1001
        self.findmaxsum(root)
        return self.maxsum
        
