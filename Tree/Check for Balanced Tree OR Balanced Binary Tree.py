#Leetcode solution
class Solution(object):
    def height(self,root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        ans = max(left, right) + 1
        return ans 
    
    def isBalanced(self, root):
        if root is None:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
    
        if abs(left - right) > 1:
            return False
        
        left_bal = self.isBalanced(root.left)
        right_bal = self.isBalanced(root.right)
        return left_bal and right_bal
        

        
#GFG solution
class Solution:
    def isBalanced(self,root):
        self.ans = True
        def height(root):
            if not root:
                return 0
            else:
                left = height(root.left)
                right = height(root.right)
                if abs(left - right) > 1:
                    self.ans = False
                return 1 + max(left, right)
        height(root)
        return self.ans
