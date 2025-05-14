from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])

        if not edges and n == 1:
            return True
        elif not edges:
            return False

        stack = [edges[0][0]]
        visited = set()
        while stack:
            node = stack.pop()
            visited.add(node)
            count = 0
            for nei in adjList[node]:
                if nei in visited and count==1:
                    return False
                elif nei in visited:
                    count+=1   
                else:
                    stack.append(nei)

        return len(visited) == n
