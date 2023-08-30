# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root == None:
            return []
        bfs_q=deque()
        bfs_q.append(root)
        level_order=[[root.val]]
        while bfs_q :
            level_nodes=[]
            level_size=len(bfs_q)
            for i in range(level_size):
                node = bfs_q.popleft()
            
                if node.left:
                    level_nodes.append(node.left.val)
                    bfs_q.append(node.left)
                if node.right:
                    level_nodes.append(node.right.val)
                    bfs_q.append(node.right)
            
            
            level_order.append(level_nodes)
        level_order.pop()
        return level_order
            

            
                
            
            
        
        
        
        
        
        
 