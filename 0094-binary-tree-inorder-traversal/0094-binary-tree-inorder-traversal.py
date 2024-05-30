# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        recursiveInorderTraversal(traversal, root)
        return traversal
        
def recursiveInorderTraversal(traversal, root):
    if root != None: 
        recursiveInorderTraversal(traversal, root.left)
        traversal.append(root.val)
        recursiveInorderTraversal(traversal, root.right)