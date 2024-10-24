"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        
        def dfs(curr):
            if curr in nodes:
                return nodes[curr]
            new = Node(curr.val)
            nodes[curr] = new
            adj = [dfs(neighbor) for neighbor in curr.neighbors]
            new.neighbors = adj
            return new
        
        return dfs(node) if node else node