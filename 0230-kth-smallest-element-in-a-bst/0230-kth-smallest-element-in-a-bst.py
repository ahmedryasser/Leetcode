# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = -1
        def inorder(root):
            nonlocal k
            nonlocal result
            if not root:
                return
            inorder(root.left)
            if k == 1 and result == -1:
                result = root.val
            elif k==1:
                return
            else:
                k-=1
            inorder(root.right)
        inorder(root)
        return result
