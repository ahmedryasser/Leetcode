# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        def inorder(root):
            nonlocal k
            nonlocal vals
            if not root:
                return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        inorder(root)
        return vals[k-1]
