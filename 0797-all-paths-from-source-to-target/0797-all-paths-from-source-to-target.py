class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def dfs(i, curr):
            if i == len(graph)-1:
                res.append(curr.copy())
            else:
                for neighbor in graph[i]:
                    curr.append(neighbor)
                    dfs(neighbor, curr)
                    curr.pop()
            
            
            
        dfs(0,[0])
        return res