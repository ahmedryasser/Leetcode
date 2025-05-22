# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def height(node,child, hei, route):
            if not node: return
            if node.val == child.val:
                return (hei,route.copy())
            else:
                route.append("l")
                left = height(node.left,child, hei+1, route)
                route.pop()
                route.append("r")
                right = height(node.right,child, hei+1, route)
                route.pop()
                if left:
                    return left
                elif right:
                    return right
        hl,l = height(root, p, 0,[])
        hr,r = height(root, q, 0,[])

        result = root
        
        for i in range(min(hl,hr)):

            if r[i] == "l" and l[i] == "l":
                
                result = result.left
            elif l[i] == "r" and r[i] == "r":
                
                result = result.right
            else:
                return result
        return result
        
        
        
            

            

