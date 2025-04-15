class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        vals = {}
        def search(index): 
            if index >= len(cost):
                return 0
            minimum = vals[index] if index in vals else min(search(index+1), search(index+2))
            vals[index] = minimum
            if index==-1:
                return  minimum
            else:
                return minimum + cost[index]
        return search(-1)
            
