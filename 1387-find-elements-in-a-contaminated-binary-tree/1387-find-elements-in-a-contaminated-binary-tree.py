# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.dfs(root, 0)
        self.tree = root
        print(self.tree)

    def dfs(self, node, num):
        if not node:
            return
        node.val = num
        self.dfs(node.left, node.val*2 +1)
        self.dfs(node.right, node.val*2 +2)
    def search(self, node, target):
        if not node or node.val> target:
            return False
        if node.val == target:
            return True
        left = self.search(node.left, target)
        right = self.search(node.right, target)
        return left or right
    def find(self, target: int) -> bool:
        return self.search(self.tree, target)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)