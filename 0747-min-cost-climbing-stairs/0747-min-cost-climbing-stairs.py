class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        vals = {}
        def bfs(index): 
            if index >= len(cost):
                return 0
            minimum = vals[index] if index in vals else min(bfs(index+1), bfs(index+2))
            vals[index] = minimum
            if index==-1:
                return  minimum
            else:
                return minimum + cost[index]
        return bfs(-1)
            
