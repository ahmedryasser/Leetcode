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
                return ([],0,0)
            left,totl,numl = dfs(node.left) 
            right,totr,numr = dfs(node.right) 
            result = left+right + [node.val]
            tot = totl+totr+node.val
            num = numl+numr+1
            if tot//num == node.val:
                res[0] += 1
            return (result,tot,num)
        dfs(root)
        return res[0]
            
