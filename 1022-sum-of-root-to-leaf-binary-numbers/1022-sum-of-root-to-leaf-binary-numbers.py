# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        vals = []
        def dfs(node, binary):
            if not node:
                return
            binary.append(str(node.val))
            if not node.left and not node.right:
                vals.append(int("".join(binary),2))
                binary.pop()
                return
            dfs(node.left, binary)
            dfs(node.right, binary)
            binary.pop()
        dfs(root, [])
        return sum(vals)