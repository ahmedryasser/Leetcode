# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            return isEqual(node1.left, node2.left) and isEqual(node1.right, node2.right)
        
        def dfs(node):
            if node is None:
                return False
            left = node.left
            right = node.right
            if isEqual(left , subRoot):
                return True
            elif isEqual(right , subRoot):
                return True
            else:
                return dfs(left) or dfs(right)
        return isEqual(root,subRoot) or dfs(root)
            
