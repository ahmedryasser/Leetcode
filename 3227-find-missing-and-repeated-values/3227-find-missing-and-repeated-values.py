class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        vals = {}
        res = []
        for arr in grid:
            for j in arr:
                vals[j] = 1 if j not in vals else 2
        for i in range(1,len(grid)**2+1):
            if i not in vals:
                res.append(i)
            elif vals[i] == 2:
                res.insert(0,i)
        return res
