# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root==None:
            return []
        bfs_q=deque()
        
        bfs_q.append(root)
        zig_zag_traversal=[[root.val]]
        right_to_left=1
        while bfs_q:
            
 #starting from level 1 
            
            level_nodes=[]
            tree_level = len(bfs_q)
           
            for i in range(tree_level):
                node= bfs_q.popleft()
                if node.left:
                    level_nodes.append(node.left.val)
                    bfs_q.append(node.left)
                if node.right:
                    level_nodes.append(node.right.val)
                    bfs_q.append(node.right)
                    
            if right_to_left % 2 ==1:
                zig_zag_traversal.append(level_nodes[::-1])
            else:
                zig_zag_traversal.append(level_nodes)
            right_to_left+=1
        zig_zag_traversal.pop()
        return zig_zag_traversal
                
                
                
            
            
        
        