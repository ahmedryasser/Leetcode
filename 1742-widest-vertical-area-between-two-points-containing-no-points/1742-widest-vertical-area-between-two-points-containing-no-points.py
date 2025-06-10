class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        vals = [val for val,_ in sorted(points, key=lambda x:x[0])]
        biggest = 0
        
        for i in range(len(points)-1):
            biggest = max(biggest, vals[i+1] - vals[i])
        
        return biggest
