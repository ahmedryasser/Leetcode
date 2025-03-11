# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1,arr2 = [],[]
        def dfs(root, arr):
            if not root:
                return None
            left = dfs(root.left,arr)
            right = dfs(root.right,arr)
            if not left and not right:
                arr.append(root.val)
            return arr
        return dfs(root1,arr1) == dfs(root2, arr2)