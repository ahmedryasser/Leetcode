# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []

        def dfs(node,path):
            if node and not node.left and not node.right:
                path.append(str(node.val))
                results.append(path.copy())
                path.pop()
                return
            elif not node:
                return
            path.append(str(node.val))
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()
        dfs(root,[])

        return ["->".join(res) for res in results]