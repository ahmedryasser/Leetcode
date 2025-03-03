# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0,0)
            left = dfs(root.left)
            right = dfs(root.right)
            rob_this = root.val + left[1] + right[1]
            not_robbin = max(left) + max(right)
            return (rob_this, not_robbin)
        
        return max(dfs(root))
        