# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, largest):
            if not root:
                return 0
            good = 1 if root.val >= largest else 0
            maxValue = max(root.val, largest )
            return good + dfs(root.left, maxValue) + dfs(root.right, maxValue)

        return dfs(root, root.val)
