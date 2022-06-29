#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    if not root:
        return []
    res = []
    res.append(root.data)
    res += preorder(root.left)
    res += preorder(root.right)
    return res
  
  
  
 #using self
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res
