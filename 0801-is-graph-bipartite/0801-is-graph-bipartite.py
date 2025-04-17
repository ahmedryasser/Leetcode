class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(position, c):
            if position in color:
                return color[position] == c
            color[position] = c
            return all(dfs(neighbor, c^1) for neighbor in graph[position])

        return all(dfs(node,0) for node in range(len(graph)) if node not in color) 