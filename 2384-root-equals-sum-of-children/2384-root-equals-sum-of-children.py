# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.left.val + root.right.val == root.val:
            return True
        else:
            return False
        # def dfs(root):
        #     if not root.left or not root.right:
        #         return 
        #     if root.left.val == root.right.val:
        #         return True
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     return left and right
        # return dfs(root)
        