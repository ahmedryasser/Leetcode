class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subtotal = []
        def dfs(i,total):
            if total == target:
                res.append(subtotal.copy())
                return
            elif i > len(candidates)-1 or total > target:
                return
            
            if total+candidates[i] <= target:
                subtotal.append(candidates[i])
                dfs(i, total+candidates[i])
                subtotal.pop()
            dfs(i+1, total)


        dfs(0,0)

        return res