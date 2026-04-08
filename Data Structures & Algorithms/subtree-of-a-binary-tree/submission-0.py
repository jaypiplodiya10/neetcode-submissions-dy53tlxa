# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not s: return True
        if not r: return False

        
        if self.sameTree(s,r): return True
        
        r_node = self.isSubtree(r.right, s)
        l_node = self.isSubtree(r.left, s)

        return (r_node or l_node)

    
    def sameTree(self, s, t):
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        if s.val != t.val:
            return False
        
        l = self.sameTree(s.left, t.left)
        r = self.sameTree(s.right, t.right)

        return (l and r)