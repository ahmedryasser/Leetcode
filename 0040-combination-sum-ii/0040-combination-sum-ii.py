class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subtotal = []
        values = set()

        def dfs(i, total):
            if total == target:
                res.append(subtotal.copy())
                return
            elif i>=len(candidates) or total > target:
                return
            new = candidates[i]
            subtotal.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subtotal.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total)
        dfs(0,0)
        return res


