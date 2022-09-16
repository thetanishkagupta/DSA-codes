class Solution(object):
    def findPathSum(self, root,pathsum):
        if root is None:
            return 0
        pathsum = pathsum * 10 + root.val
        if(root.left is None and root.right is None):
            return pathsum
        return self.findPathSum(root.left,pathsum) + self.findPathSum(root.right,pathsum)
    
    def sumNumbers(self,root):
        return self.findPathSum(root,0)
