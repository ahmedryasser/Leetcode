from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        count = 0
        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)


        for i in range(n):
            if i not in visited:
                dfs(i)
                count +=1
        
        return count
            