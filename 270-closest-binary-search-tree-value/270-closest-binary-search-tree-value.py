# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, tree: Optional[TreeNode], target: float) -> int:
        diff = abs(target-tree.val)
        closest= tree.val
        orig = tree.val
        while (tree != None):
            if target > tree.val:
            
                if abs(target - tree.val) < diff:
                    closest=tree.val
                    diff = abs(target - tree.val)
                tree = tree.right   
            elif target < tree.val:
            
                if abs(target - tree.val) < diff:
                    closest=tree.val
                    diff = abs(target - tree.val)
                tree = tree.left    
            else:
                return tree.val
        return closest