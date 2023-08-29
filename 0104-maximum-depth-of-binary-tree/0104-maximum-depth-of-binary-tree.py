# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recursion(root):
            
            if root == None:
                return 0 
            
            left=recursion(root.left)
            right=recursion(root.right)
            return max(left,right)+1
        return recursion(root)
         
            
        
        