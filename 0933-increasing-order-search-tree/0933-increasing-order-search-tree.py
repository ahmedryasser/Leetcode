# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new = TreeNode(0)
        head = new
        def dfs(node):
            nonlocal new
            if not node:
                return
            dfs(node.left)
            new.right = TreeNode(node.val)
            new = new.right
            dfs(node.right)
            
            
        dfs(root)
        return head.right
