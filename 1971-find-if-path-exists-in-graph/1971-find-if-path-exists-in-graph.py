from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        
        seen = set()
        
        def dfs(i):
            if i in seen:
                return False
            seen.add(i)
            if i == destination:
                return True
            for side in d[i]:
                if dfs(side):
                    return True
            return False
        
        return dfs(source)