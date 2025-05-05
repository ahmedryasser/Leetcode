# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = defaultdict(list)
        def level(node, lvl):
            if not node:
                return
            level(node.left, lvl+1)
            traversal[lvl].append(node.val)
            level(node.right,lvl+1)
        
        level(root,0)
        return [traversal[i] for i in range(len(traversal.values()))]

