# function should return the count of total number of non leaf nodes in the tree
class Solution:
    def countNonLeafNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return (1 + self.countNonLeafNodes(root.left) + self.countNonLeafNodes(root.right))
      
