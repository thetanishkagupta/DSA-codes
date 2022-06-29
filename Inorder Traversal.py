#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        if not root:
            return []
        res = []
        res += self.InOrder(root.left)
        res.append(root.data)
        res += self.InOrder(root.right)
        return res
