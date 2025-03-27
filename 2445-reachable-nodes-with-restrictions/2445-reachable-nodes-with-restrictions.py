from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = defaultdict(list)
        visited = set(restricted)
        count = 0
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        def dfs(node):
            nonlocal count
            if node in visited:
                return 0
            count+=1
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        dfs(0)
        return count
            
