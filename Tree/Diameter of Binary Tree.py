class Solution(object):
    diameter = 0
    def findheight(self, root):
        if root is None:
            return 0
        left_height = self.findheight(root.left)
        right_height = self.findheight(root.right)
        curr_diameter = left_height + right_height + 1
        self.diameter = max(curr_diameter , self.diameter)
        return max(left_height , right_height) + 1
        
    def diameterOfBinaryTree(self, root):
        self.findheight(root)
        return self.diameter
