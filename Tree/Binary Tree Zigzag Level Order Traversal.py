class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return None
        
        res =[[]]
        level = 0
        self.zigzag(root,level,res)
        return res
        
    def zigzag(self,root,level,res):
        if root is None:
            return None
        if len(res) < level + 1:
            res.append([])
        if level % 2 == 1:
            res[level].append(root.val)
        elif level % 2 == 0:
            res[level].insert(0, root.val)
                
        self.zigzag(root.right,level+1,res)
        self.zigzag(root.left,level+1,res)
        
        
