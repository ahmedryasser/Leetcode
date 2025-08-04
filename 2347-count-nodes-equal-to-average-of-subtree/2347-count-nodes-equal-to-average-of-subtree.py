# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node):
            if not node:
                return []
            left = dfs(node.left) 
            right = dfs(node.right) 
            result = left+right + [node.val]
            if sum(result)//len(result) == node.val:
                res[0] +=1
            return result
        dfs(root)
        return res[0]
            
