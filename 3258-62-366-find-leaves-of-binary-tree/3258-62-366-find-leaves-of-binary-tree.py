# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return -1
            left_height = bfs(root.left)
            right_height = bfs(root.right)
            current_height =  max(left_height,right_height) +1
            if current_height == len(result):
                result.append([])
            result[current_height].append(root.val)
            return current_height
            
        result = []
        bfs(root)
        return result