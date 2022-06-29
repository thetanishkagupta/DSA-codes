#Function to return a list containing the postorder traversal of the tree.
def postOrder(root):
    if not root:
        return []
    res = []
    res += postOrder(root.left)
    res += postOrder(root.right)
    res.append(root.data)
    return res
  
  
  
  #using self
  class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res
